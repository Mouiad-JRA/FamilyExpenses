from django.urls import path

from expense.views import delete_expense, ExpenseCreateView, ExpenseEditView, search_expenses, \
    MaterialCreateView, ExpenseListView, MaterialListView, MaterialEditView, delete_material, OutlayTypeListView, \
    OutlayTypeCreateView, OutlayTypeEditView, delete_outlaytype
from django.views.decorators.csrf import csrf_exempt
app_name = "expenses-dash"
urlpatterns = [
    path('', ExpenseListView.as_view(), name='expenses'),
    path('search-expenses', csrf_exempt(search_expenses), name='search_expenses'),
    path('add-expense/', ExpenseCreateView.as_view(), name='add_expense'),
    path('edit-expense/<int:pk>', ExpenseEditView.as_view(), name='edit_expense'),
    path('delete-expense/<int:pk>', delete_expense, name='delete_expense'),
    path('materials/', MaterialListView.as_view(), name='materials'),
    path('add-material/', MaterialCreateView.as_view(), name='add_material'),
    path('edit-material/<int:pk>', MaterialEditView.as_view(), name='edit_material'),
    path('delete-material/<int:pk>', delete_material, name='delete_material'),

    path('outlaytypes/', OutlayTypeListView.as_view(), name='outlaytypes'),
    path('add-outlaytype/', OutlayTypeCreateView.as_view(), name='add_outlaytype'),
    path('edit-outlaytype/<int:pk>', OutlayTypeEditView.as_view(), name='edit_outlaytype'),
    path('delete-outlaytypes/<int:pk>', delete_outlaytype, name='delete_outlaytype'),
]

