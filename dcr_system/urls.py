from django.urls import path
from dcr_system import views

urlpatterns = [
    path('product-type/list', views.ProductTypeListView.as_view(), name='product-type-list'),
    path('product-type/create', views.ProductTypeCreateView.as_view(), name='product-type-create'),
    path('product-type/detail/<int:pk>', views.ProductTypeDetailView.as_view(), name='product-type-detail'),
    path('product-type/update/<int:pk>', views.ProductTypeUpdateView.as_view(), name='product-type-update'),
    path('product-type/delete/<int:pk>', views.ProductTypeDestroyView.as_view(), name='product-type-delete'),


    path('product-information/list', views.ProductInformationListView.as_view(), name='product-information-list'),
    path('product-information/create', views.ProductInformationCreateView.as_view(), name='product-information-create'),
    path('product-information/detail/<int:pk>', views.ProductInformationDetailView.as_view(), name='product-information-detail'),
    path('product-information/update/<int:pk>', views.ProductInformationUpdateView.as_view(), name='product-information-update'),
    path('product-information/delete/<int:pk>', views.ProductInformationDeleteView.as_view(), name='product-information-delete'),

    

]