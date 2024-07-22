
from django.db import models

  
   

# Create your models here.
from django.db import models
import uuid
class admin_user(models.Model):
    customer_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer_name = models.CharField(max_length=100, blank=True, null=True)
    customer_email = models.EmailField(unique=True, blank=True, null=True)
     # Authentication
    customer_password = models.CharField(max_length=128, blank=True, null=True) 
    customer_phone_number = models.CharField(max_length=15, blank=True, null=True)
    customer_address = models.TextField( blank=True, null=True)
    customer_created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
   
    

    
  
