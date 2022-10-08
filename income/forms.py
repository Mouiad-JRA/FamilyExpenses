from django import forms
from django.core.exceptions import ValidationError
from django.utils.timezone import now

from income.models import Income, Source


class IncomeCreationForm(forms.ModelForm):
    amount = forms.DecimalField(decimal_places=3)

    class Meta:
        model = Income
        fields = (
            "amount",
            "source",
            "date",
            "description",
        )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(IncomeCreationForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        outlay = super(IncomeCreationForm, self).save(commit=False)

        outlay.price = self.cleaned_data['amount']
        outlay.description = self.cleaned_data['description']
        outlay.date = self.cleaned_data['date']
        outlay.outlay_type = Source.objects.filter(name=self.cleaned_data['source']).first()
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
        amount = self.cleaned_data['amount']
        if amount < 0:
            raise ValidationError("You can't choose a negative price")
        return amount
