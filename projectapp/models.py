from django.db import models

# Create your models here.
class registration_tb(models.Model):
    email=models.CharField(max_length=200,default='')
    password=models.CharField(max_length=200,default='')
    re_password=models.CharField(max_length=200,default='')
    first_name=models.CharField(max_length=200,default='')
    last_name=models.CharField(max_length=200,default='')
    gender=models.CharField(max_length=200,default='')
    country=models.CharField(max_length=200,default='')