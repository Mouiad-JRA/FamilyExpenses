
from django.urls import path

from .views import RegisterView,UserLogin, UsernameValidationView, UserEmailValidationView,\
    UserFamilyValidationView, UserHeadValidationView, PasswordValidationView, LogoutView
from django.views.decorators.csrf import csrf_exempt

app_name = "account"
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='login'),
    path('validate-username/', csrf_exempt(UsernameValidationView.as_view()), name='validate-username'),
    path('validate-email/', csrf_exempt(UserEmailValidationView.as_view()), name='validate-email'),
    path('validate-family-name/', csrf_exempt(UserFamilyValidationView.as_view()), name='validate-family-name'),
    path('validate-family-head/', csrf_exempt(UserHeadValidationView.as_view()), name='validate-family-head'),
    path('validate-password/', csrf_exempt(PasswordValidationView.as_view()), name='validate-password'),
    path('logout/', LogoutView.as_view(), name='logout'),

]

