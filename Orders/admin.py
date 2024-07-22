from django.contrib import admin



# Register your models here.
from django.contrib import admin

# Register your models here.
from Orders.models import Order
@admin.register(Order)  # Pass the model to register
class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
