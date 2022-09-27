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
    success_url = reverse_lazy('')
    form_class = CustomUserCreationForm
    success_message = "Your profile was created successfully"

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("")
        messages.error(request, "Unsuccessful registration. Invalid information.")

        form = CustomUserCreationForm()
        return render(request=request, template_name="accounts/register.html", context={"register_form": form})


def register_request(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = CustomUserCreationForm()
    return render(request=request, template_name="accounts/register.html", context={"register_form": form})


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse("account:login"))
