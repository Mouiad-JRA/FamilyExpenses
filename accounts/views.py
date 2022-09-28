from django.shortcuts import render

from django.views.generic.edit import CreateView
from django.contrib.auth import login, logout

from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.views import View

from accounts.forms import CustomUserCreationForm


class RegisterView(CreateView):
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('add_expense')
    form_class = CustomUserCreationForm
    success_message = "Your profile was created successfully"


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse("account:register"))
