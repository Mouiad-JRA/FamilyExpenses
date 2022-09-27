from django.shortcuts import render
from django.views import View

from django.contrib.auth import login, logout

from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy

from django.utils.translation import gettext_lazy as _
from django.views import View

from .models import User


class RegisterView(View):
    def get(self, request):
        return render(request, 'accounts/register.html')


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse("account:login"))
