from django.contrib import admin
from dcr_system.models import ProductInformation, ProductType


admin.site.register(ProductType)
admin.site.register(ProductInformation)