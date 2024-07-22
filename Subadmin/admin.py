from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from Subadmin.models import Subadmin
# Register your models here.
@admin.register(Subadmin)
class ProductAdmin(admin.ModelAdmin):
   
    list_display = [field.name for field in Subadmin._meta.fields] 
