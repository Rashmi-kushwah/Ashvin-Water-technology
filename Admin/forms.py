# from django import forms
# from Product.models import Product, Main_Category, Sub_Category

# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = '__all__'

# class MainCategoryForm(forms.ModelForm):
#     class Meta:
#         model = Main_Category
#         fields = '__all__'

# class SubCategoryForm(forms.ModelForm):
#     class Meta:
#         model = Sub_Category
#         fields = '__all__'



from django import forms
from Product.models import Product, Main_Category, Sub_Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'sub_title': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'mrp': forms.NumberInput(attrs={'class': 'form-control'}),
            'sku_code': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'main_category': forms.Select(attrs={'class': 'form-control'}),
            'sub_category': forms.Select(attrs={'class': 'form-control'}),
            'model_name': forms.TextInput(attrs={'class': 'form-control'}),
            'img1': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'img2': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'img3': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'img4': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'img5': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'img6': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'img7': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'img8': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'warranty': forms.TextInput(attrs={'class': 'form-control'}),
            'technology': forms.TextInput(attrs={'class': 'form-control'}),
            'feature': forms.TextInput(attrs={'class': 'form-control'}),
            'product_type': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'active_product': forms.CheckboxInput(attrs={'class': 'custom-control-input', 'id': 'customSwitch'}),
            'order_status': forms.TextInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'qty1': forms.NumberInput(attrs={'class': 'form-control'}),
            'qty2': forms.NumberInput(attrs={'class': 'form-control'}),
            'qty3': forms.NumberInput(attrs={'class': 'form-control'}),
            'qty4': forms.NumberInput(attrs={'class': 'form-control'}),
            'qty5': forms.NumberInput(attrs={'class': 'form-control'}),
            'qty6': forms.NumberInput(attrs={'class': 'form-control'}),
            'qty7': forms.NumberInput(attrs={'class': 'form-control'}),
            'qty8': forms.NumberInput(attrs={'class': 'form-control'}),
            'qty9': forms.NumberInput(attrs={'class': 'form-control'}),
            'qty10': forms.NumberInput(attrs={'class': 'form-control'}),
            'weight': forms.TextInput(attrs={'class': 'form-control'}),
            'dimensions': forms.TextInput(attrs={'class': 'form-control'}),
            'installation_type': forms.TextInput(attrs={'class': 'form-control'}),
            'storage_capacity': forms.TextInput(attrs={'class': 'form-control'}),
            'purification_modules': forms.Textarea(attrs={'class': 'form-control'}),
            'input_water_pressure': forms.TextInput(attrs={'class': 'form-control'}),
            'input_water_temperature': forms.TextInput(attrs={'class': 'form-control'}),
            'input_water_chlorine_max': forms.TextInput(attrs={'class': 'form-control'}),
            'input_water_tds': forms.TextInput(attrs={'class': 'form-control'}),
            'uv_lamp': forms.TextInput(attrs={'class': 'form-control'}),
            'uv_lamp_life': forms.TextInput(attrs={'class': 'form-control'}),
            'power_consumption': forms.TextInput(attrs={'class': 'form-control'}),
            'operating_input_voltage': forms.TextInput(attrs={'class': 'form-control'}),
            'included_in_box': forms.Textarea(attrs={'class': 'form-control'}),
            'product_warranty': forms.TextInput(attrs={'class': 'form-control'}),
        }

class MainCategoryForm(forms.ModelForm):
    class Meta:
        model = Main_Category
        fields = '__all__'
        widgets = {
            'main_Categorytype': forms.TextInput(attrs={'class': 'form-control'}),
            'main_Category': forms.TextInput(attrs={'class': 'form-control'}),
        }

class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = Sub_Category
        fields = '__all__'
        widgets = {
            'main_category': forms.Select(attrs={'class': 'form-control'}),
            'Sub_Categorytype': forms.TextInput(attrs={'class': 'form-control'}),
            'Sub_Category': forms.TextInput(attrs={'class': 'form-control'}),
        }






# Galleryapp/forms.py

from django import forms
from Galleryapp.models import Page

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['bg_img1', 'title1_h3', 'title1_p',
                  'bg_img2', 'title2_h3', 'title2_p',
                  'bg_img3', 'title3_h3', 'title3_p',
                  'bg_img4', 'title4_h3', 'title4_p',
                  'bg_img5', 'title5_h3', 'title5_p',
                  'bg_img6', 'title6_h3', 'title6_p',
                  'bg_img7', 'title7_h3', 'title7_p',
                  'bg_img8', 'title8_h3', 'title8_p',
                  'bg_img9', 'title9_h3', 'title9_p',
                  'bg_img10', 'title10_h3', 'title10_p',
                  'bg_img11', 'title11_h3', 'title11_p',
                  'bg_img12', 'title12_h3', 'title12_p',
                  'bg_img13', 'title13_h3', 'title13_p']
