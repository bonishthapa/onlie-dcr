from rest_framework import serializers
from salary_expenses.models import SalaryExpense
from user.serializers import UserSerializer

class SalaryExpensesSerializer(serializers.ModelSerializer):
    created_by = UserSerializer()
    updated_by = UserSerializer()
    class Meta:
        model = SalaryExpense
        fields = ['id', 'date', 'TA', 'DA', 'others', 'remarks', 'miscellaneous', 'visited_area',
                  'created_by', 'created_date', 'updated_by', 'updated_date', 'status1', 'status2']
        read_only_fields = ['creator_id','updated_by']           