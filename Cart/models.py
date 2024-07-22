from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class addcart(models.Model):
      
    Product_id = models.CharField(max_length=50, null=True, blank=True)
    user_uid = models.CharField(max_length=50,null=True, blank=True)
    sku_code = models.CharField(max_length=50,null=True, blank=True)
    title= models.CharField(max_length=30,null=True, blank=True)
    color = models.CharField(max_length=50,null=True, blank=True)  # Rang
    img1 = models.ImageField(upload_to='photos/', blank=True, null=True,max_length=200, )
    qty = models.CharField(max_length=20,null=True, blank=True)
    size = models.CharField(max_length=30,null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    mrp = models.IntegerField(null=True, blank=True)
    delivery_charges = models.CharField(max_length=30,null=True, blank=True)
    discount = models.CharField(max_length=30,null=True, blank=True)
    total_amount = models.CharField(max_length=30,null=True, blank=True)
    total_qty = models.CharField(max_length=30,null=True, blank=True)