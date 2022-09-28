import json

from django.http import JsonResponse

from django.views.generic.edit import CreateView
from django.contrib.auth import login, logout

from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy

from django.views import View
from django.core.validators import validate_email
from accounts.forms import CustomUserCreationForm
from accounts.models import User


class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        if any(char.isdigit() for char in username) or not str(username).isalnum():
            return JsonResponse({"username_error": "please Enter valid username."}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({"username_error": "This username is already taken, please try another."}, status=400)

        return JsonResponse({"username_valid": True})


class UserEmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        try:
            validate_email(email)
        except:
            return JsonResponse({"email_error": "please Enter valid Email."}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({"email_error": "This Email is already taken, please try another."}, status=400)

        return JsonResponse({"useremail_valid": True})


class UserFamilyValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        family_name = data['family_name']

        if any(char.isdigit() for char in family_name) or not str(family_name).isalnum():
            return JsonResponse({"family_name_error": "please enter a Valid family name"}, status=400)

        return JsonResponse({"userfamily_name_valid": True})


class RegisterView(CreateView):
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('add_expense')
    form_class = CustomUserCreationForm
    success_message = "Your profile was created successfully"


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse("account:register"))
