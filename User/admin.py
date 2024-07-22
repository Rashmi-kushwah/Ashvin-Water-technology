from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from User.models import Eurekaforbes_User
@admin.register(Eurekaforbes_User)  # Pass the model to register
class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Eurekaforbes_User._meta.fields]