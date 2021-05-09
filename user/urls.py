from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from user import views

urlpatterns = [
    path('',views.home),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


    path('designation/list', views.DesignationListView.as_view(),name='designation'),
    path('designation/create', views.DesignationCreateView.as_view(),name='designation-create'),
    path('designation/detail/<int:pk>', views.DesignationDetailView.as_view(),name='designation-detail'),
    path('designation/update/<int:pk>', views.DesignationUpdateView.as_view(),name='designation-update'),
    path('designation/delete/<int:pk>', views.DesignationDeleteView.as_view(),name='designation-delete'),


    path('user/list', views.UserListView.as_view(),name='user-list'),
    path('user/create', views.UserCreateView.as_view(),name='user-create'),
    path('user/detail/<int:pk>', views.UserDetailView.as_view(),name='user-detail'),
    path('user/update/<int:pk>', views.UserUpdateView.as_view(),name='user-update'),
    path('user/delete/<int:pk>', views.UserDeleteView.as_view(),name='user-delete'),


    path('client-type/list', views.ClientTypeListView.as_view(), name='client-type-list'),
    path('client-type/create', views.ClientTypeCreateView.as_view(), name='client-type-create'),
    path('client-type/detail/<int:pk>', views.ClientTypeDetailView.as_view(), name='client-type-detail'),
    path('client-type/update/<int:pk>', views.ClientTypeUpdateView.as_view(), name='client-type-update'),
    path('client-type/delete/<int:pk>', views.ClientTypeDeleteView.as_view(), name='client-type-delete'),


    path('client-table/list', views.ClientTableListView.as_view(), name='client-table-list'),
    path('client-table/create', views.ClientTableCreateView.as_view(), name='client-table-create'),
    path('client-table/detail/<int:pk>', views.ClientTableDetailView.as_view(), name='client-table-detail'),
    path('client-table/update/<int:pk>', views.ClientTableUpdateView.as_view(), name='client-table-update'),
    path('client-table/delete/<int:pk>', views.ClientTableDeleteView.as_view(), name='client-table-delete'),

    path('user-control-table/list', views.UserControlTableListView.as_view(), name='user-control-table-list'),
    path('user-control-table/create', views.UserControlTableCreateView.as_view(), name='user-control-table-create'),
    path('user-control-table/detail/<int:pk>', views.UserControlTableDetailView.as_view(), name='user-control-table-detail'),
    path('user-control-table/update/<int:pk>', views.UserControlTableUpdateView.as_view(), name='user-control-table-update'),
    path('user-control-table/delete/<int:pk>', views.UserControlTableDeleteView.as_view(), name='user-control-table-delete'),

]