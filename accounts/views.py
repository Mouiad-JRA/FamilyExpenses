import json

from django.contrib import messages
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import LoginView
from django.db.models import Q

from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from django.views.generic.edit import CreateView
from django.contrib.auth import logout

from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.core.validators import validate_email
from accounts.forms import CustomUserCreationForm
from accounts.models import User, Family
from django.core.mail import send_mail, BadHeaderError




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
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('expenses-dash:expenses')

    def post(self, request, *args, **kwargs):
        print(request.POST)
        print(self.get_form().errors)
        return super(UserLogin, self).post(request, *args, **kwargs)


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse("account:login"))


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "accounts/password/password_reset_email.html"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com', [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("/password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="accounts/password/password_reset.html",
                  context={"password_reset_form": password_reset_form})
