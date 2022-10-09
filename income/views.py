from braces.views import UserFormKwargsMixin
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from income.forms import IncomeCreationForm
from income.models import Income, Source
from userperferences.models import UserPerference


class IncomeListView(ListView):
    template_name = "incomes/incomes.html"
    success_url = "income-dash:incomes"
    queryset = Income.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        incomes = self.queryset.filter(owner=self.request.user)
        paginator = Paginator(incomes, 5)
        page_number = self.request.GET.get('page')
        page_obj = Paginator.get_page(paginator, page_number)
        try:
            currency = UserPerference.objects.get(user=self.request.user).currency
        except:
            currency = None
        ctx = {
            'incomes': incomes,
            'page_obj': page_obj,
            'currency': currency
        }
        return ctx


class IncomeCreateView(LoginRequiredMixin, UserFormKwargsMixin, CreateView):
    template_name = "incomes/add_income.html"
    form_class = IncomeCreationForm

    def get_context_data(self, **kwargs):
        context = super(IncomeCreateView, self).get_context_data(**kwargs)
        sources = Source.objects.all()
        context['sources'] = sources
        context['values'] = self.request.POST
        return context

    def get_success_url(self):
        messages.success(self.request, 'Income Saved successfully')
        return reverse('income-dash:incomes')


class IncomeEditView(LoginRequiredMixin, UserFormKwargsMixin, UpdateView):
    template_name = "incomes/edit_income.html"
    model = Income
    form_class = IncomeCreationForm

    def get_context_data(self, **kwargs):
        context = super(IncomeEditView, self).get_context_data(**kwargs)
        sources = Source.objects.all()
        context['sources'] = sources
        return context

    def get_success_url(self):
        messages.success(self.request, 'Income Update successfully')
        return reverse('income-dash:incomes')


def delete_income(request, pk):
    expense = Income.objects.get(pk=pk)
    expense.delete()
    messages.success(request, 'Income has been deleted successfully')
    return redirect("income-dash:incomes")

