from django.db import models
from django.apps import AppConfig
from django.conf import settings
# Create your models here.

#
class GetAmount(models.Model):
    value = models.CharField(max_length=1000,default=None)
    name = models.CharField(max_length=100,default ="x")
    
    #__Str__ method is a string representation of the object i.e a name
    def __str__(self):
        return self.name

    class Meta: 
        app_label = "payments"