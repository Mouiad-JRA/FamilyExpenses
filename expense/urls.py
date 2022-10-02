
from django.urls import path

from expense.views import index, add_expense, expense_edit

app_name = "expenses-dash"
urlpatterns = [
    path('', index, name='expenses'),
    path('add-expense/', add_expense, name='add_expense'),
    path('edit-expense/<int:id>', expense_edit, name='edit'),
]

