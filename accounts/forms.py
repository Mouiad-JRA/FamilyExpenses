from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from django import forms
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class CustomUserEditForm(UserChangeForm):
    picture = forms.ImageField(label=_("Picture/Logo"), required=False)


class CustomUserCreationForm(UserCreationForm):
    picture = forms.ImageField(label=_("Picture/Logo"), required=False)

    def clean_email(self):
        email = self.cleaned_data["email"]

        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email

        raise ValidationError(self.error_messages["duplicate_username"])
