from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models

class Page(models.Model):
   
    # background_image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True)
    bg_img1 = models.ImageField(upload_to='photos/', blank=True, null=True, max_length=200)
    title1_h3= models.CharField(max_length=500, blank=True, null=True)
    title1_p= models.CharField(max_length=500, blank=True, null=True)
    bg_img2 = models.ImageField(upload_to='photos/', blank=True, null=True, max_length=200)
    title2_h3= models.CharField(max_length=500, blank=True, null=True)
    title2_p= models.CharField(max_length=500, blank=True, null=True)
    bg_img3 = models.ImageField(upload_to='photos/', blank=True, null=True, max_length=200)
    title3_h3= models.CharField(max_length=500, blank=True, null=True)
    title3_p= models.CharField(max_length=500, blank=True, null=True)
    bg_img4 = models.ImageField(upload_to='photos/', blank=True, null=True, max_length=200)
    title4_h3= models.CharField(max_length=500, blank=True, null=True)
    title4_p= models.CharField(max_length=500, blank=True, null=True)
    bg_img5 = models.ImageField(upload_to='photos/', blank=True, null=True, max_length=200)
    title5_h3= models.CharField(max_length=500, blank=True, null=True)
    title5_p= models.CharField(max_length=500, blank=True, null=True)
    bg_img6 = models.ImageField(upload_to='photos/', blank=True, null=True, max_length=200)
    title6_h3= models.CharField(max_length=500, blank=True, null=True)
    title6_p= models.CharField(max_length=500, blank=True, null=True)
    bg_img7 = models.ImageField(upload_to='photos/', blank=True, null=True, max_length=200)
    title7_h3= models.CharField(max_length=500, blank=True, null=True)
    title7_p= models.CharField(max_length=500, blank=True, null=True)
    bg_img8 = models.ImageField(upload_to='photos/', blank=True, null=True, max_length=200)
    title8_h3= models.CharField(max_length=500, blank=True, null=True)
    title8_p= models.CharField(max_length=500, blank=True, null=True) 
    bg_img9 = models.ImageField(upload_to='photos/', blank=True, null=True, max_length=200)
    title9_h3= models.CharField(max_length=500, blank=True, null=True)
    title9_p= models.CharField(max_length=500, blank=True, null=True)
    bg_img10 = models.ImageField(upload_to='photos/', blank=True, null=True, max_length=200)
    title10_h3= models.CharField(max_length=500, blank=True, null=True)
    title10_p= models.CharField(max_length=500, blank=True, null=True)
    bg_img11 = models.ImageField(upload_to='photos/', blank=True, null=True, max_length=200)
    title11_h3= models.CharField(max_length=500, blank=True, null=True)
    title11_p= models.CharField(max_length=500, blank=True, null=True)
    bg_img12 = models.ImageField(upload_to='photos/', blank=True, null=True, max_length=200)
    title12_h3= models.CharField(max_length=500, blank=True, null=True)
    title12_p= models.CharField(max_length=500, blank=True, null=True)
    bg_img13 = models.ImageField(upload_to='photos/', blank=True, null=True, max_length=200)
    title13_h3= models.CharField(max_length=500, blank=True, null=True)
    title13_p= models.CharField(max_length=500, blank=True, null=True)


