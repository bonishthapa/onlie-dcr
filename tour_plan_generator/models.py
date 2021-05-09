from django.db import models
from user.models import User

# Create your models here.

class TourPlan(models.Model):
    date = models.DateField()
    morining_station = models.CharField(max_length=250)
    evening_station = models.CharField(max_length=250)
    morning_station_type = models.CharField(max_length=250)
    evening_station_type = models.CharField(max_length=250)
    creator_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tour_plan_creator')
    approver_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tour_plan_approver')
    status1 = models.CharField(max_length=250)
    status2 = models.CharField(max_length=250)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tour_plan_updated_by')
    updated_date = models.DateTimeField(auto_now=True)



class TourPlanHigher(models.Model):
    morning_supervised = models.ForeignKey(User, on_delete=models.CASCADE, related_name='morning_supervised')
    evening_supervised = models.ForeignKey(User, on_delete=models.CASCADE, related_name='evening_supervised')
    date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tour_plan_higher_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tour_plan_higher_updated_by')
    updated_date = models.DateTimeField(auto_now=True)

       