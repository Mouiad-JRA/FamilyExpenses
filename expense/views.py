from django.contrib import messages
from django.shortcuts import render, redirect

from expense.models import OutlayType, Material, Outlay


def index(request):
    expenses = Outlay.objects.filter(owner=request.user)
    ctx = {
        'outlays': expenses
    }
    return render(request, 'expenses/index.html', ctx)


def add_expense(request):
    outlay_types = OutlayType.objects.all()
    materials = Material.objects.all()
    ctx = {
        'outlay_types': outlay_types,
        'materials': materials,
        'values': request.POST,
    }
    if request.method == 'GET':
        return render(request, 'expenses/add_expense.html', ctx)
    if request.method == 'POST':
        price = request.POST['price']
        description = request.POST['description']
        date = request.POST['date']
        outlay_type = request.POST['outlay_type']
        material = request.POST['material']

        if not price:
            messages.error(request, 'Price is required')
            return render(request, 'expenses/add_expense.html', ctx)
        if not description:
            messages.error(request, 'Description is required')
            return render(request, 'expenses/add_expense.html', ctx)
        if not date:
            messages.error(request, 'Date is required')
            return render(request, 'expenses/add_expense.html', ctx)
        if outlay_type and material:
            outlay_type = OutlayType.objects.get(name=outlay_type)
            material = Material.objects.get(name=material)
            Outlay.objects.create(owner=request.user, price=price, date=date, description=description,
                                  material=material, outlay_type=outlay_type)
        messages.success(request, 'Outlay Saved successfully')
        return redirect("expenses-dash:expenses")

