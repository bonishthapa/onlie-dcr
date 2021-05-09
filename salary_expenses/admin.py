from django.contrib import admin
from salary_expenses.models import SalaryExpense

@admin.register(SalaryExpense)
class SalaryExpensesAdmin(admin.ModelAdmin):
        list_display = ['date']
