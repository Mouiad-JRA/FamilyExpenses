
from django.urls import path

from .views import index

app_name = "preference"
urlpatterns = [
    path('', index, name='preferences'),

]

