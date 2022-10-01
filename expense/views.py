from django.shortcuts import render

from expense.models import OutlayType, Material


def index(request):
    outlay_type = OutlayType.objects.all()
    materials = Material.objects.all()
    return render(request, 'expenses/index.html')


def add_expense(request):
    outlay_types = OutlayType.objects.all()
    materials = Material.objects.all()
    ctx={
        'outlay_types': outlay_types,
        'materials' :  materials
    }
    return render(request, 'expenses/add_expense.html', ctx)
