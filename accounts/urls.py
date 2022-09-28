
from django.urls import path

from .views import RegisterView, UsernameValidationView, UserEmailValidationView, LogoutView
from django.views.decorators.csrf import csrf_exempt

app_name = "account"
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('validate-username/', csrf_exempt(UsernameValidationView.as_view()), name='validate-username'),
    path('validate-email/', csrf_exempt(UserEmailValidationView.as_view()), name='validate-email'),
    path('logout/', LogoutView.as_view(), name='logout'),

]

