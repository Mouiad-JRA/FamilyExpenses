from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView

# from expense.forms import OutlayCreationForm, OutlayEditForm
from expense.forms import OutlayCreationForm, OutlayEditForm
from expense.models import OutlayType, Material, Outlay
from django.core.paginator import Paginator

import json
from django.http import JsonResponse


def search_expenses(request):
    if request.method == 'POST':
        search_string = json.loads(request.body).get('searchText')
        expense = Outlay.objects.filter(
            price__istartswith=search_string,
            owner=request.user
        ) | Outlay.objects.filter(
            date__istartswith=search_string,
            owner=request.user
        ) | Outlay.objects.filter(
            description__icontains=search_string,
            owner=request.user
        ) | Outlay.objects.filter(
            outlay_type__name__icontains=search_string,
            owner=request.user
        ) | Outlay.objects.filter(
            material__name__icontains=search_string,
            owner=request.user
        )
        data = expense.values()

    return JsonResponse(list(data), safe=False)


def index(request):
    expenses = Outlay.objects.filter(owner=request.user)
    paginator = Paginator(expenses, 5)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    ctx = {
        'outlays': expenses,
        'page_obj': page_obj
    }
    return render(request, 'expenses/index.html', ctx)


class ExpenseCreateView(CreateView):
    template_name = "expenses/add_expense.html"
    success_url = 'expenses-dash:expenses'

    def get_form(self, form_class=None):
        if self.request.method == 'POST':
            return OutlayCreationForm(self.request.POST, user=self.request.user)
        return OutlayCreationForm(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(ExpenseCreateView, self).get_context_data(**kwargs)
        outlay_types = OutlayType.objects.all()
        materials = Material.objects.all()
        context['outlay_types'] = outlay_types
        context['materials'] = materials
        context['values'] = self.request.POST
        context['user'] = self.request.user
        return context

    def get_success_url(self):
        messages.success(self.request, 'Outlay Saved successfully')
        return reverse('expenses-dash:expenses')


class ExpenseEditView(UpdateView):
    template_name = "expenses/edit_expense.html"
    queryset = Outlay.objects.all()

    def get_form(self, form_class=None):
        if self.request.method == 'POST':
            return OutlayEditForm(self.request.POST, user=self.request.user)
        return OutlayEditForm(user=self.request.user)

    def get_object(self, queryset=None):
        return Outlay.objects.filter(pk=self.kwargs.get('pk')).first()

    def get_context_data(self, **kwargs):
        context = super(ExpenseEditView, self).get_context_data(**kwargs)
        outlay_types = OutlayType.objects.all()
        materials = Material.objects.all()
        context['outlay_types'] = outlay_types
        context['materials'] = materials
        context['user'] = self.request.user
        return context

    def get_success_url(self):
        messages.success(self.request, 'Outlay Update successfully')
        return redirect('expenses-dash:expenses')


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
    return render(request, 'expenses/add_expense.html', ctx)


def expense_edit(request, id):
    expense = Outlay.objects.get(pk=id)
    outlay_types = OutlayType.objects.all()
    materials = Material.objects.all()
    ctx = {
        "expense": expense,
        "outlay_types": outlay_types,
        "materials": materials
    }
    if request.method == 'GET':
        return render(request, 'expenses/edit_expense.html', ctx)

    elif request.method == 'POST':
        price = request.POST['price']
        description = request.POST['description']
        date = request.POST['date']
        outlay_type = request.POST['outlay_type']
        material = request.POST['material']

        if not price:
            messages.error(request, 'Price is required')
            return render(request, 'expenses/edit_expense.html', ctx)
        if not description:
            messages.error(request, 'Description is required')
            return render(request, 'expenses/edit_expense.html', ctx)
        if not date:
            messages.error(request, 'Date is required')
            return render(request, 'expenses/edit_expense.html', ctx)
        if outlay_type and material:
            outlay_type = OutlayType.objects.get(name=outlay_type)
            material = Material.objects.get(name=material)
            expense.owner = request.user
            expense.price = price
            expense.date = date
            expense.description = description
            expense.outlay_type = outlay_type
            expense.material = material
            expense.save()
        messages.success(request, 'Outlay Updated successfully')
        return redirect("expenses-dash:expenses")


def delete_expense(request, pk):
    expense = Outlay.objects.get(pk=pk)
    expense.delete()
    messages.success(request, 'Outlay has been deleted successfully')
    return redirect("expenses-dash:expenses")
