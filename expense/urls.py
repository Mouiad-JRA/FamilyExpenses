from django.urls import path

from expense.views import index, add_expense, expense_edit, delete_expense, search_expenses
from django.views.decorators.csrf import csrf_exempt

app_name = "expenses-dash"
urlpatterns = [
    path('', index, name='expenses'),
    path('add-expense/', add_expense, name='add_expense'),
    path('edit-expense/<int:id>', expense_edit, name='edit'),
    path('delete-expense/<int:id>', delete_expense, name='delete'),
    path('search-expenses', csrf_exempt(search_expenses), name='search_expenses'),
]
