from django import forms

from expense.models import Outlay


class OutlayForm(forms.ModelForm):
    class Meta:
        model = Outlay
        fields = '__all__'

    def save(self, commit=True):
        outlay = super(OutlayForm, self).save(commit=False)

        outlay.price = self.cleaned_data['price']
        outlay.description = self.cleaned_data['description']
        outlay.date = self.cleaned_data['date']
        outlay.outlay_type = self.cleaned_data['outlay_type']
        outlay.material = self.cleaned_data['material']

        if commit:
            outlay.save()
        return outlay
