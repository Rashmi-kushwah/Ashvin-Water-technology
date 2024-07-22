from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from Cart.models import addcart
@admin.register(addcart)  # Pass the model to register
class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in addcart._meta.fields]
