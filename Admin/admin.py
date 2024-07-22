from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from Admin.models import admin_user
@admin.register(admin_user)  # Pass the model to register
class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in admin_user._meta.fields]



