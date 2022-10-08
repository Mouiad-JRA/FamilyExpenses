from django.urls import path

from expense.views import index, add_expense, expense_edit, delete_expense, ExpenseCreateView, ExpenseEditView, search_expenses
from django.views.decorators.csrf import csrf_exempt
app_name = "expenses-dash"
urlpatterns = [
    path('', index, name='expenses'),
    path('search-expenses', csrf_exempt(search_expenses), name='search_expenses'),
    path('add-expense/', ExpenseCreateView.as_view(), name='add_expense'),
    path('edit-expense/<int:pk>', ExpenseEditView.as_view(), name='edit'),
    path('delete-expense/<int:pk>', delete_expense, name='delete'),
]

