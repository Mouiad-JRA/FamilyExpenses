from django.urls import path

from income.views import IncomeListView, IncomeEditView, delete_income, IncomeCreateView

app_name = "income-dash"
urlpatterns = [

    # Expense
    path('', IncomeListView.as_view(), name='incomes'),
    path('add-income/', IncomeCreateView.as_view(), name='add_income'),
    path('edit-income/<int:pk>', IncomeEditView.as_view(), name='edit_income'),
    path('delete-income/<int:pk>', delete_income, name='delete_income'),
    ]
