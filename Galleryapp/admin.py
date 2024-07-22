from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from Galleryapp.models import Page
# Register your models here.
@admin.register(Page)
class ProductAdmin(admin.ModelAdmin):
   
    list_display = [field.name for field in Page._meta.fields] 