from django.db import models
from user.models import User

# Create your models here.

class SalaryExpense(models.Model):
    date = models.DateField()
    TA = models.FloatField()
    DA = models.FloatField()
    others = models.FloatField()
    remarks = models.CharField(max_length=250)
    miscellaneous = models.FloatField()
    visited_area = models.CharField(max_length=250)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='salary_expense_created_by')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='salary_expense_updated_by')
    updated_date = models.DateTimeField(auto_now=True)
    status1 = models.CharField(max_length=250)
    status2 = models.CharField(max_length=250)


