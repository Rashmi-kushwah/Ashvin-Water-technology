from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
# from django.contrib import admin
# from products.models import *
# # Register your models here.
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
   
#     list_display = [field.name for field in Product._meta.fields] 

# @admin.register(Main_Category)
# class ProductAdmin(admin.ModelAdmin):
   
#     list_display = [field.name for field in Main_Category._meta.fields] 


# @admin.register(Sub_Category)
# class ProductAdmin(admin.ModelAdmin):
   
#     list_display = [field.name for field in Sub_Category._meta.fields]    

from Product.models import Product

from django.contrib import admin
from .models import Main_Category, Sub_Category, Product

# # Register Main_Category with customization
# @admin.register(Main_Category)
# class MainCategoryAdmin(admin.ModelAdmin):
#     list_display = ('main_Categorytype', 'main_Category')
#     search_fields = ('main_Categorytype', 'main_Category')

# # Register Sub_Category with customization
# @admin.register(Sub_Category)
# class SubCategoryAdmin(admin.ModelAdmin):
#     list_display = ('Sub_Categorytype', 'Sub_Category')
#     search_fields = ('Sub_Categorytype', 'Sub_Category')

# # Register Product with customization
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = (
#         'name', 'title', 'price', 'mrp', 'brand', 'Category', 'main_Category', 'Sub_Category', 
#         'stock', 'active_product'
#     )
#     search_fields = ('name', 'title', 'brand', 'sku_code', 'Category', 'main_Category', 'Sub_Category')
#     list_filter = ('active_product', 'brand', 'main_Category', 'Sub_Category')
#     readonly_fields = ('Product_id',)
    
#     fieldsets = (
#         (None, {
#             'fields': ('name', 'title', 'sub_title', 'price', 'mrp', 'sku_code', 'brand', 'color', 'Category', 'main_Category', 'Sub_Category', 'Model_name')
#         }),
#         ('Images', {
#             'fields': ('img1', 'img2', 'img3', 'img4', 'img5', 'img6', 'img7', 'img8')
#         }),
#         ('Stock and Active Status', {
#             'fields': ('stock', 'active_product')
#         }),
#         ('Quantities', {
#             'fields': ('qty1', 'qty2', 'qty3')
#         }),
#         ('Specifications', {
#             'fields': (
#                 'weight', 'dimensions', 'installation_type', 'storage_capacity', 'purification_modules', 
#                 'input_water_pressure', 'input_water_temperature', 'input_water_chlorine_max', 
#                 'input_water_tds', 'uv_lamp', 'uv_lamp_life', 'power_consumption', 'operating_input_voltage'
#             )
#         }),
#         ('Description and Warranty', {
#             'fields': ('description', 'included_in_box', 'product_warranty')
#         }),
#     )

from django.contrib import admin
from .models import Main_Category, Sub_Category, Product

@admin.register(Main_Category)
class MainCategoryAdmin(admin.ModelAdmin):
    list_display = ('main_Categorytype', 'main_Category')
    search_fields = ('main_Categorytype', 'main_Category')

@admin.register(Sub_Category)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('Sub_Categorytype', 'Sub_Category')
    search_fields = ('Sub_Categorytype', 'Sub_Category')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'title', 'sub_title', 'price', 'mrp', 'sku_code', 'brand', 'color', 
        'main_category', 'sub_category', 'model_name', 'warranty', 
        'technology', 'feature', 'product_type', 'description', 'active_product', 
        'stock', 'qty1', 'qty2', 'qty3', 'weight', 'dimensions', 'installation_type', 
        'storage_capacity', 'purification_modules', 'input_water_pressure', 
        'input_water_temperature', 'input_water_chlorine_max', 'input_water_tds', 
        'uv_lamp', 'uv_lamp_life', 'power_consumption', 'operating_input_voltage', 
        'included_in_box', 'product_warranty'
    )
    search_fields = ('name', 'sku_code', 'brand', 'main_category__main_Categorytype', 'sub_category__Sub_Categorytype')
