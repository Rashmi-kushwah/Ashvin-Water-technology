from django.db import models
import uuid
# Create your models here.
class Subadmin(models.Model):
    Sub_admin_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Sub_admin_name = models.CharField(max_length=100)
    Sub_admin_email = models.EmailField()
    Sub_admin_password = models.CharField(max_length=100)
 
    Sub_admin_address = models.CharField(max_length=200)
    Sub_admin_pincode = models.CharField(max_length=100)
    Sub_admin_ac = models.CharField(max_length=100)
    Sub_admin_ifc = models.CharField(max_length=100)
    Sub_admin_no = models.CharField(max_length=100)
    Sub_admin_2no = models.CharField(max_length=100)

