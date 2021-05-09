from django.contrib import admin
from report_generator.models import LeaveReport, AdminReport, DailyCallReport, DcrHigher, SalesReport

admin.site.register(LeaveReport)
admin.site.register(AdminReport)
admin.site.register(DailyCallReport)
admin.site.register(DcrHigher)

@admin.register(SalesReport)
class SalesReportAdmin(admin.ModelAdmin):
    list_display = ['date']
