import os
import json

from django.conf import settings
from django.contrib import messages
from django.shortcuts import render

from userperferences.models import UserPerference


def index(request):
    currencies = []
    path = os.path.join(settings.BASE_DIR, 'currencies.json')
    with open(path) as file:
        data = json.load(file)
        for key, value in data.items():
            currencies.append({"name": key, "value": value})
    user_perferences = UserPerference.objects.get(user=request.user) if \
        UserPerference.objects.filter(user=request.user).exists() else None
    if request.method == 'GET':

        return render(request, 'perferences/index.html',
                      {'currencies': currencies, 'user_perferences': user_perferences})
    else:
        currency = request.POST['currency']
        if user_perferences:
            user_perferences.currency = currency
            user_perferences.save()
        else:
            UserPerference.objects.create(user=request.user, currency=currency)
        messages.success(request, f'Your currency has been changed to {currency}')
        return render(request, 'perferences/index.html',
                      {'currencies': currencies, 'user_perferences': user_perferences})
