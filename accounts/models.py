from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_admin= models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    approved = models.BooleanField('Approved', default = False)
    age = models.IntegerField(null=True)
    profile_pic= models.ImageField(blank=True)
    credentials_img = models.ImageField(blank=True)
    
