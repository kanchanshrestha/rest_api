from django.db import models

# Create your models here.

class Customer(models.Model):
    username=models.CharField(max_length=25,null=True,blank=True)
    name=models.CharField(max_length=25,null=True,blank=True)
    address=models.CharField(max_length=25,null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
class Meta:
        db_table="Customer"