from django.contrib import admin
from user.models import Designation, User, ClientTable, ClientType,UserControlTable

# Register your models here.
admin.site.register(User)
admin.site.register(Designation)
admin.site.register(ClientType)
@admin.register(ClientTable)
class ClientTableAdmin(admin.ModelAdmin):
    list_display = ['name','client_type_id','user_id','updated_by','updated_date']

@admin.register(UserControlTable)
class UserControlTableAdmin(admin.ModelAdmin):
    list_display = ['supervisor','supervised']