from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
import uuid

class Eurekaforbes_User(models.Model):
    user_uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=15,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    phone_number = models.CharField(max_length=15,blank=True,null=True)
    Created_date = models.DateField(auto_now_add=True)
    password = models.CharField(max_length=255)  # Added password field
    otp = models.CharField(max_length=6, blank=True, null=True)  # Added OTP field
    verify_code = models.CharField(blank=True, null=True, max_length=6,) 