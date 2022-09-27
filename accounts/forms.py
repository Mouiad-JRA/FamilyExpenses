from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from django import forms
from django.utils.translation import gettext_lazy as _

from accounts.models import Family

User = get_user_model()


class CustomUserEditForm(UserChangeForm):
    picture = forms.ImageField(label=_("Picture/Logo"), required=False)


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    picture = forms.ImageField(label=_("Picture/Logo"), required=False)

    class Meta:
        model = User
        fields = ("username", "email", "picture", "password1", "password2", "family", "head")

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.family = self.cleaned_data['family']
        user.head = self.cleaned_data['head']
        Family.objects.get_or_create(family_name=user.family)
        if commit:
            user.save()
        return user

    def clean_email(self):
        email = self.cleaned_data["email"]

        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email

        raise ValidationError(self.error_messages["duplicate_username"])
