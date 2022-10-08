from django import forms
from django.core.exceptions import ValidationError
from django.utils.timezone import now

from .models import Outlay, OutlayType, Material


class OutlayCreationForm(forms.ModelForm):
    price = forms.DecimalField(decimal_places=3)
    class Meta:
        model = Outlay
        fields = (
            "material",
            "outlay_type",
            "price",
            "date",
            "description",
        )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(OutlayCreationForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        outlay = super(OutlayCreationForm, self).save(commit=False)

        outlay.price = self.cleaned_data['price']
        outlay.description = self.cleaned_data['description']
        outlay.date = self.cleaned_data['date']
        outlay.outlay_type = OutlayType.objects.filter(name=self.cleaned_data['outlay_type']).first()
        outlay.material = Material.objects.filter(name=self.cleaned_data['material']).first()
        outlay.owner = self.user

        if commit:
            outlay.save()
        return outlay

    def clean_date(self):
        date = self.cleaned_data['date']
        if date > now().date():
            raise ValidationError("You can't choose date in Future")
        return date

    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise ValidationError("You can't choose a negative price")
        return price



class MaterialCreationForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = (
            "name",
            "is_service",
            "description",
        )


class OutlayTypeCreationForm(forms.ModelForm):
    class Meta:
        model = OutlayType
        fields = (
            "name",
            "description",
        )