from allauth.account.forms import LoginForm
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
    family_name = forms.CharField(required=True, max_length=255)
    is_head = forms.BooleanField(required=True)
    error_css_class = "error"

    class Meta:
        model = User
        fields = ("username", "email", "picture", "password1", "password2", "family_name", "is_head")
        exclude = ("family", "head")

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)

        user.email = self.cleaned_data['email']
        family_name = self.cleaned_data['family_name']
        is_head = self.cleaned_data['is_head']
        family, created = Family.objects.get_or_create(family_name=family_name)
        user.family = family
        if is_head:
            user.head = family
        user.name = user.username
        if commit:
            if self.cleaned_data["password1"]:
                user.set_password(self.cleaned_data["password1"])
            user.save()
        return user



