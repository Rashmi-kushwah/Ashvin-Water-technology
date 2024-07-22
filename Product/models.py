from django.db import models

# Create your models here.
from django.db import models
import uuid

class Main_Category(models.Model):
    main_Categorytype = models.CharField(max_length=100, blank=True, null=True)
    main_Category = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.main_Categorytype  if self.main_Categorytype else ""
   

class Sub_Category(models.Model):
    main_category = models.ForeignKey(Main_Category, on_delete=models.SET_NULL, blank=True, null=True)
    Sub_Categorytype = models.CharField(max_length=100, blank=True, null=True)
    Sub_Category = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.Sub_Category  if self.Sub_Category else ""
 



class Product(models.Model):
    Product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=300, blank=True, null=True)
    sub_title = models.CharField(max_length=300, blank=True, null=True)
    price = models.DecimalField(max_digits=30, decimal_places=2, blank=True, null=True)
    mrp = models.IntegerField(blank=True, null=True)
    sku_code = models.CharField(max_length=100, blank=True, null=True)
    brand = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    main_category = models.ForeignKey(Main_Category, on_delete=models.SET_NULL, blank=True, null=True,max_length=50,)
    sub_category = models.ForeignKey(  Sub_Category, on_delete=models.SET_NULL, blank=True, null=True,max_length=50,)
    model_name = models.CharField(max_length=20, blank=True, null=True)
    img1 = models.ImageField(upload_to='photos/', blank=True, null=True, max_length=200)
    img2 = models.ImageField(upload_to='photos/', blank=True, null=True, max_length=200)
    img3 = models.ImageField(upload_to='photos/', blank=True, null=True, max_length=200)
    img4 = models.ImageField(upload_to='photos/', blank=True, null=True, max_length=200)
    img5 = models.ImageField(upload_to='photos/', blank=True, null=True, max_length=200)
    img6 = models.ImageField(upload_to='photos/', blank=True, null=True, max_length=200)
    img7 = models.ImageField(upload_to='photos/', blank=True, null=True, max_length=200)
    img8 = models.ImageField(upload_to='photos/', blank=True, null=True, max_length=200)
    warranty = models.CharField(max_length=50, blank=True, null=True)
    technology = models.CharField(max_length=100, blank=True, null=True)
    feature = models.CharField(max_length=100, blank=True, null=True)
    product_type = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    active_product = models.BooleanField(default=True, blank=True, null=True)
    order_status=models.CharField(max_length=100,null=True, blank=True)
    stock = models.PositiveIntegerField(default=0, blank=True, null=True)
    qty1 = models.IntegerField(default=0, blank=True, null=True)
    qty2 = models.IntegerField(default=0, blank=True, null=True)
    qty3 = models.IntegerField(default=0, blank=True, null=True)
    qty4 = models.IntegerField(default=0, blank=True, null=True)
    qty5 = models.IntegerField(default=0, blank=True, null=True)
    qty6 = models.IntegerField(default=0, blank=True, null=True)
    qty7 = models.IntegerField(default=0, blank=True, null=True)
    qty8 = models.IntegerField(default=0, blank=True, null=True)
    qty9 = models.IntegerField(default=0, blank=True, null=True)
    qty10 = models.IntegerField(default=0, blank=True, null=True)
    weight = models.CharField(max_length=50, verbose_name='Weight', blank=True, null=True)
    dimensions = models.CharField(max_length=100, verbose_name='Dimensions (WxDxH)', blank=True, null=True)
    installation_type = models.CharField(max_length=100, verbose_name='Installation Type', blank=True, null=True)
    storage_capacity = models.CharField(max_length=50, verbose_name='Storage Capacity', blank=True, null=True)
    purification_modules = models.TextField(verbose_name='Purification Modules', blank=True, null=True)
    input_water_pressure = models.CharField(max_length=50, verbose_name='Input Water Pressure', blank=True, null=True)
    input_water_temperature = models.CharField(max_length=50, verbose_name='Input Water Temperature', blank=True, null=True)
    input_water_chlorine_max = models.CharField(max_length=50, verbose_name='Input Water Chlorine (Max)', blank=True, null=True)
    input_water_tds = models.CharField(max_length=50, verbose_name='Input Water TDS', blank=True, null=True)
    uv_lamp = models.CharField(max_length=50, verbose_name='UV Lamp', blank=True, null=True)
    uv_lamp_life = models.CharField(max_length=50, verbose_name='UV Lamp Life', blank=True, null=True)
    power_consumption = models.CharField(max_length=50, verbose_name='Power Consumption', default='Unknown', blank=True, null=True)
    operating_input_voltage = models.CharField(max_length=50, verbose_name='Operating Input Voltage', blank=True, null=True)
    included_in_box = models.TextField(verbose_name='Included in the Box', blank=True, null=True)
    product_warranty = models.CharField(max_length=50, verbose_name='Product Warranty', blank=True, null=True)


    sub_admin =models.CharField(max_length=100,null=True, blank=True)

    def __str__(self):
        return self.name if self.name else str(self.Product_id)
