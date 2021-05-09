from django.contrib import admin
from tour_plan_generator.models import TourPlan, TourPlanHigher

@admin.register(TourPlanHigher)
class TourPlanHigherAdmin(admin.ModelAdmin):
    list_display = ['date']

@admin.register(TourPlan)
class TourPlanAdmin(admin.ModelAdmin):
    list_display = ['date']