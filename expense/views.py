from django.contrib import messages
from django.shortcuts import render

from expense.models import OutlayType, Material


def index(request):
    outlay_type = OutlayType.objects.all()
    materials = Material.objects.all()
    return render(request, 'expenses/index.html')


def add_expense(request):
    outlay_types = OutlayType.objects.all()
    materials = Material.objects.all()
    ctx = {
        'outlay_types': outlay_types,
        'materials': materials,
        'values': request.POST,
    }
    # if request.method == 'GET':


    if request.method == 'POST':
        price = request.POST['price']
        description = request.POST['description']
        date = request.POST['date']
        if not price:
            messages.error(request, 'Price is required')
            return render(request, 'expenses/add_expense.html', ctx)
        if not description:
            messages.error(request, 'Description is required')
            return render(request, 'expenses/add_expense.html', ctx)
        if not date:
            messages.error(request, 'Date is required')
            return render(request, 'expenses/add_expense.html', ctx)

    return render(request, 'expenses/add_expense.html', ctx)
