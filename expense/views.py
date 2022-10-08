from braces.views import UserFormKwargsMixin, LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView

from expense.forms import OutlayCreationForm
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


class ExpenseCreateView(LoginRequiredMixin, UserFormKwargsMixin, CreateView):
    template_name = "expenses/add_expense.html"
    success_url = 'expenses-dash:expenses'
    form_class = OutlayCreationForm

    def get_context_data(self, **kwargs):
        context = super(ExpenseCreateView, self).get_context_data(**kwargs)
        outlay_types = OutlayType.objects.all()
        materials = Material.objects.all()
        context['outlay_types'] = outlay_types
        context['materials'] = materials
        context['values'] = self.request.POST
        return context

    def get_success_url(self):
        messages.success(self.request, 'Outlay Saved successfully')
        return reverse('expenses-dash:expenses')


class ExpenseEditView(LoginRequiredMixin, UserFormKwargsMixin, UpdateView):
    template_name = "expenses/edit_expense.html"
    model = Outlay
    form_class = OutlayCreationForm

    def get_context_data(self, **kwargs):
        context = super(ExpenseEditView, self).get_context_data(**kwargs)
        outlay_types = OutlayType.objects.all()
        materials = Material.objects.all()
        context['outlay_types'] = outlay_types
        context['materials'] = materials
        return context

    def get_success_url(self):
        messages.success(self.request, 'Outlay Update successfully')
        return reverse('expenses-dash:expenses')


def delete_expense(request, pk):
    expense = Outlay.objects.get(pk=pk)
    expense.delete()
    messages.success(request, 'Outlay has been deleted successfully')
    return redirect("expenses-dash:expenses")
