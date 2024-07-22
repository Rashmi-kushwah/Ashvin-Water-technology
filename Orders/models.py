from django.db import models

# Create your models here.

# Create your models here.
from django.db import models

class Order(models.Model):
    Product_id = models.CharField(max_length=50, null=True, blank=True)
    user_uid = models.CharField(max_length=50,null=True, blank=True)

    first_name = models.CharField(max_length=100 ,null=True, blank=True)
    last_name = models.CharField(max_length=100 ,null=True, blank=True)
    mobile_number = models.CharField(max_length=10,null=True, blank=True)
    email = models.EmailField()

    house_no = models.CharField(max_length=10, blank=True, null=True)
    street = models.CharField(max_length=100, blank=True, null=True)
    street1 = models.CharField(max_length=100, blank=True, null=True)
    street2 = models.CharField(max_length=100, blank=True, null=True)
    pin_code = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, default='India',blank=True, null=True)
    region = models.CharField(max_length=50, blank=True, null=True)


    order_id =models.CharField(max_length=100,null=True, blank=True)  # State name
    order_date=models.CharField(max_length=100,null=True, blank=True)  # State name
    tracking_id=models.CharField(max_length=100,null=True, blank=True)  # State name
    tracking_link=models.CharField(max_length=100,null=True, blank=True)  # State name
    order_status=models.CharField(max_length=100,null=True, blank=True)  # State name
    total_amount = models.CharField(max_length=30,null=True, blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=2,null=True, blank=True)
    qty = models.CharField(max_length=30,null=True, blank=True)
    img1 = models.ImageField(upload_to='photos/', blank=True, null=True,max_length=200, )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


