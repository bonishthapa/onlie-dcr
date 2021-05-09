from django.urls import path
from report_generator import views

urlpatterns = [

    path('leave-report/list', views.LeaveReportListView.as_view(), name='leave-report-list'),
    path('leave-report/create', views.LeaveReportCreateView.as_view(), name='leave-report-create'),
    path('leave-report/detail/<int:p>', views.LeaveReportDetailView.as_view(), name='leave-report-detail'),
    path('leave-report/update/<int:pk>', views.LeaveReportUpdateView.as_view(), name='leave-report-update'),
    path('leave-report/delete/<int:pk>', views.LeaveReportDeleteView.as_view(), name='leave-report-delete'),


    path('admin-report/list', views.AdminReportListView.as_view(), name='admin-report-list'),
    path('admin-report/create', views.AdminReportCreateView.as_view(), name='admin-report-create'),
    path('admin-report/detail/<int:pk>', views.AdminReportDetailView.as_view(), name='admin-report-detail'),
    path('admin-report/update/<int:pk>', views.AdminReportUpdateView.as_view(), name='admin-report-update'),
    path('admin-report/delete/<int:pk>', views.AdminReportDeleteView.as_view(), name='admin-report-delete'),


    path('daily-call-report/list', views.DailyCallReportListView.as_view(), name='dailycall-report-list'),
    path('daily-call-report/create', views.DailyCallReportCreateView.as_view(), name='dailycall-report-create'),
    path('daily-call-report/detail/<int:pk>', views.DailyCallReportDetailView.as_view(), name='dailycall-report-detail'),
    path('daily-call-report/update/<int:pk>', views.DailyCallReportUpdateView.as_view(), name='dailycall-report-update'),
    path('daily-call-report/delete/<int:pk>', views.DailyCallReportDeleteView.as_view(), name='dailycall-report-delete'),


    path('dcr-higher/list', views.DCRHigherListView.as_view(), name='dcr-higher-list'),
    path('dcr-higher/create', views.DCRHigherCreateView.as_view(), name='dcr-higher-create'),
    path('dcr-higher/detail/<int:pk>', views.DCRHigherDetailView.as_view(), name='dcr-higher-detail'),
    path('dcr-higher/update/<int:pk>', views.DCRHigherUpdateView.as_view(), name='dcr-higher-update'),
    path('dcr-higher/delete/<int:pk>', views.DCRHigherDeleteView.as_view(), name='dcr-higher-delete'),


    path('sales-report/list', views.SalesReportListView.as_view(), name='sales-report-list'),
    path('sales-report/create', views.SalesReportCreateView.as_view(), name='sales-report-create'),
    path('sales-report/detail/<int:pk>', views.SalesReportDetailView.as_view(), name='sales-report-detail'),
    path('sales-report/update/<int:pk>', views.SalesReportUpdateView.as_view(), name='sales-report-update'),
    path('sales-report/delete/<int:pk>', views.SalesReportDeleteView.as_view(), name='sales-report-delete'),
]    