from django.urls import path
from salary_expenses import views

urlpatterns = [
    path('salary-expenses/list', views.SalaryExpensesListView.as_view(), name='salary-expenses-list'),
    path('salary-expenses/create', views.SalaryExpensesCreateView.as_view(), name='salary-expenses-create'),
    path('salary-expenses/detail/<int:pk>', views.SalaryExpensesDetailView.as_view(), name='salary-expenses-detail'),
    path('salary-expenses/update/<int:pk>', views.SalaryExpensesUpdateView.as_view(), name='salary-expenses-update'),
    path('salary-expenses/delete/<int:pk>', views.SalaryExpensesDeleteView.as_view(), name='salary-expenses-delete'),
]