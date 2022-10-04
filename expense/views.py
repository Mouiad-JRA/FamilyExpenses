from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView

# from expense.forms import OutlayCreationForm, OutlayEditForm
from expense.models import OutlayType, Material, Outlay


def index(request):
    expenses = Outlay.objects.filter(owner=request.user)
    ctx = {
        'outlays': expenses
    }
    return render(request, 'expenses/index.html', ctx)

#
# class ExpenseCreateView(CreateView):
#     form_class = OutlayCreationForm
#     template_name = "expenses/add_expense.html"
#     success_url = 'expenses-dash:expenses'
#
#     def get_context_data(self, **kwargs):
#         context = super(ExpenseCreateView, self).get_context_data(**kwargs)
#         outlay_types = OutlayType.objects.all()
#         materials = Material.objects.all()
#         context['outlay_types'] = outlay_types
#         context['materials'] = materials
#         context['values'] = self.request.POST
#         return context
#
#     def get_success_url(self):
#         messages.success(self.request, 'Outlay Saved successfully')
#         return reverse('expenses-dash:expenses')
#
#
# class ExpenseEditView(DetailView):
#     form_class = OutlayEditForm
#     template_name = "expenses/edit_expense.html"
#     queryset = Outlay.objects.all()
#
#     # def get_object(self, queryset=None):
#     def get_context_data(self, **kwargs):
#         context = super(ExpenseEditView, self).get_context_data(**kwargs)
#         outlay_types = OutlayType.objects.all()
#         materials = Material.objects.all()
#         context['outlay_types'] = outlay_types
#         context['materials'] = materials
#         context['values'] = self.request.POST
#         return context
#
#     def get_success_url(self):
#         messages.success(self.request, 'Outlay Update successfully')
#         return redirect('expenses-dash:expenses')


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
