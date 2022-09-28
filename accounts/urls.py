
from django.urls import path

from .views import RegisterView, UserValidationView, LogoutView
from django.views.decorators.csrf import csrf_exempt

app_name = "account"
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('validate/', csrf_exempt(UserValidationView.as_view()), name='validate'),
    path('logout/', LogoutView.as_view(), name='logout'),

]

