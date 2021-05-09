from django.urls import path
from tour_plan_generator import views

urlpatterns = [
    path('tour-plan/list', views.TourPlanListView.as_view(), name='tour-plan-list'),
    path('tour-plan/create', views.TourPlanCreateView.as_view(), name='tour-plan-create'),
    path('tour-plan/detail/<int:pk>', views.TourPlanDetailView.as_view(), name='tour-plan-detail'),
    path('tour-plan/update/<int:pk>', views.TourPlanUpdateView.as_view(), name='tour-plan-update'),
    path('tour-plan/delete/<int:pk>', views.TourPlanDeleteView.as_view(), name='tour-plan-delete'),

    path('tour-plan-higher/list', views.TourPlanHigherListView.as_view(), name='tour-plan-higher-list'),
    path('tour-plan-higher/create', views.TourPlanHigherCreateView.as_view(), name='tour-plan-higher-create'),
    path('tour-plan-higher/detail/<int:pk>', views.TourPlanHigherDetailView.as_view(), name='tour-plan-higher-detail'),
    path('tour-plan-higher/update/<int:pk>', views.TourPlanHigherUpdateView.as_view(), name='tour-plan-higher-update'),
    path('tour-plan-higher/delete/<int:pk>', views.TourPlanHigherDeleteView.as_view(), name='tour-plan-higher-delete'),
]