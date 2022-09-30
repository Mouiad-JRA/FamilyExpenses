import json

from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.forms import forms
from django.http import JsonResponse

from django.views.generic.edit import CreateView
from django.contrib.auth import login, logout, authenticate

from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.core.validators import validate_email
from accounts.forms import CustomUserCreationForm, UserLoginForm
from accounts.models import User, Family
from django.core.mail import EmailMessage, send_mail
from allauth.account.forms import LoginForm


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


class UserHeadValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        print("momo")
        print(data)
        is_head = data['is_head']
        family_name = data['family_name']
        if not family_name:
            return JsonResponse({"family_name_error": "This cannot be empty, please add a family name"}, status=400)
        family = Family.objects.filter(family_name=family_name)
        if User.objects.filter(head=family).exists() and is_head:
            return JsonResponse({"family_name_error": "You Can not Be the head of this Family, because it's already "
                                                      "have one"}, status=400)

        return JsonResponse({"family_name_valid": True})


class PasswordValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        print("moomo")
        print(data)
        password1 = data['passwordone']
        password2 = data['password2']
        if password2 != password1:
            return JsonResponse({"password_error": "The two passwords doesn't match, please enter same password"},
                                status=400)

        return JsonResponse({"password_valid": True})


class RegisterView(CreateView):
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')
    form_class = CustomUserCreationForm
    success_message = _("Your profile was created successfully")

    def post(self, request, *args, **kwargs):
        family_name = request.POST['family_name']

        password1 = request.POST['password1']
        password2 = request.POST['password2']
        username = request.POST['username']
        picture = request.POST['picture']
        email = request.POST['email']
        is_head = ''
        try:
            is_head = request.POST['is_head']
        except:
            print("This is not the Head of Family")
        ctx = {
            'user': request.POST
        }
        family, created = Family.objects.get_or_create(family_name=family_name)
        if is_head and User.objects.filter(head=family).exists():
            messages.error(request, "You Can not Be the head of this Family, because it's already have one")
            return render(request, "accounts/register.html", context=ctx)

        if User.objects.filter(email=email).exists():
            messages.error(request, "This Email is already taken, please try another.")
            return render(request, "accounts/register.html", context=ctx)

        if User.objects.filter(username=username).exists():
            messages.error(request, "This Username is already taken, please try another.")
            return render(request, "accounts/register.html", context=ctx)

        if password2 != password1:
            messages.error(request, "The two passwords doesn't match, please enter same password")
            return render(request, "accounts/register.html", context=ctx)

        send_mail(
            'Welcoming Login Account Email',
            'You have registered in out site, login in here',
            'noreply@gmail.com',
            [request.POST['email']],

        )
        if is_head:
            user = User.objects.create_user(username=username, name=username, email=email, picture=picture,
                                            family=family, head=family)
        else:
            user = User.objects.create_user(username=username, name=username, email=email, picture=picture,
                                            family=family)
        user.set_password(password1)
        user.save()

        messages.success(request, self.success_message)

        return super(RegisterView, self).post(request, *args, **kwargs)


class UserLogin(LoginView):
    model = User
    form_class = UserLoginForm
    template_name = "accounts/login.html"
    success_url = "/"


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse("account:register"))
