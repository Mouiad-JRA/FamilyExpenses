from braces.views import UserFormKwargsMixin, LoginRequiredMixin
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView

from accounts.models import User
from expense.forms import OutlayCreationForm, MaterialCreationForm, OutlayTypeCreationForm
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


class ExpenseListView(ListView):
    template_name = "expenses/expenses.html"
    success_url = 'expenses-dash:expenses'
    queryset = Outlay.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        expenses = self.queryset.filter(owner=self.request.user)
        paginator = Paginator(expenses, 5)
        page_number = self.request.GET.get('page')
        page_obj = Paginator.get_page(paginator, page_number)
        ctx = {
            'outlays': expenses,
            'page_obj': page_obj
        }
        return ctx


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


class OutlayTypeListView(ListView):
    template_name = "expenses/outlaytype.html"
    success_url = 'expenses-dash:outlaytypes'
    queryset = OutlayType.objects.all()

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_head_of_fmaily():
            messages.error(request, "You are not the head of the Family So you can't see/add or edit any materials")
            return render(request, "expenses/expenses.html")
        return super(OutlayTypeListView, self).get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        outlaytypes = self.queryset
        paginator = Paginator(outlaytypes, 5)
        page_number = self.request.GET.get('page')
        page_obj = Paginator.get_page(paginator, page_number)
        ctx = {
            'outlaytypes': outlaytypes,
            'page_obj': page_obj
        }
        return ctx


class OutlayTypeCreateView(LoginRequiredMixin, CreateView):
    template_name = "expenses/add_outlaytype.html"
    form_class = OutlayTypeCreationForm
    success_url = reverse_lazy("expenses-dash:outlaytypes")

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_head_of_fmaily():
            messages.error(request, "You are not the head of the Family So you can't see/add or edit any materials")
            return render(request, "expenses/expenses.html")
        return super(OutlayTypeCreateView, self).get(request, *args, **kwargs)


class OutlayTypeEditView(LoginRequiredMixin, UpdateView):
    template_name = "expenses/edit_outlaytype.html"
    form_class = OutlayTypeCreationForm
    success_url = reverse_lazy("expenses-dash:outlaytypes")
    queryset = OutlayType.objects.all()

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_head_of_fmaily():
            messages.error(request, "You are not the head of the Family So you can't see/add or edit any materials")
            return render(request, "expenses/expenses.html")
        return super(OutlayTypeEditView, self).get(request, *args, **kwargs)


def delete_outlaytype(request, pk):
    material = OutlayType.objects.get(pk=pk)
    material.delete()
    messages.success(request, 'OutlayType has been deleted successfully')
    return redirect("expenses-dash:outlaytypes")



class MaterialListView(ListView):
    template_name = "expenses/materials.html"
    success_url = 'expenses-dash:materials'
    queryset = Material.objects.all()

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_head_of_fmaily():
            messages.error(request, "You are not the head of the Family So you can't see/add or edit any materials")
            return render(request, "expenses/expenses.html")
        return super(MaterialListView, self).get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        materials = self.queryset
        paginator = Paginator(materials, 5)
        page_number = self.request.GET.get('page')
        page_obj = Paginator.get_page(paginator, page_number)
        ctx = {
            'materials': materials,
            'page_obj': page_obj
        }
        return ctx


class MaterialCreateView(LoginRequiredMixin, CreateView):
    template_name = "expenses/add_material.html"
    form_class = MaterialCreationForm
    success_url = reverse_lazy("expenses-dash:materials")

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_head_of_fmaily():
            messages.error(request, "You are not the head of the Family So you can't see/add or edit any materials")
            return render(request, "expenses/expenses.html")
        return super(MaterialCreateView, self).get(request, *args, **kwargs)


class MaterialEditView(LoginRequiredMixin, UpdateView):
    template_name = "expenses/edit_materials.html"
    form_class = MaterialCreationForm
    success_url = reverse_lazy("expenses-dash:materials")
    queryset = Material.objects.all()

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_head_of_fmaily():
            messages.error(request, "You are not the head of the Family So you can't see/add or edit any materials")
            return render(request, "expenses/expenses.html")
        return super(MaterialEditView, self).get(request, *args, **kwargs)


def delete_material(request, pk):
    material = Material.objects.get(pk=pk)
    material.delete()
    messages.success(request, 'Material has been deleted successfully')
    return redirect("expenses-dash:materials")
