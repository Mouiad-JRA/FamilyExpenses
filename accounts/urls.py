
from django.urls import path

from .views import RegisterView, register_request

urlpatterns = [
    path('register/', register_request, name='register'),

]

