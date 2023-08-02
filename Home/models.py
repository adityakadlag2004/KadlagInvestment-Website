from django.db import models

# Create your models here.


class CustomerForm(models.Model):
    name = models.CharField(max_length=550)
    email = models.CharField(max_length=300)
    phno = models.CharField(max_length=12)
    services = models.CharField(max_length=600)
    
