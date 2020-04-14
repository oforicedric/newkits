from django.db import models
from django.apps import AppConfig
from django.conf import settings
# Create your models here.



class Club(models.Model):
    team = models.CharField(max_length=120)
    league = models.CharField(max_length=120)
    pic = models.ImageField() #needs to be img
    gender = models.CharField(max_length=120,default="male")

    class Meta:
        app_label = 'data'

    def __str__(self):# reprsents the name of individual records
        return self.team




class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    #last_scrape = models.DateTimeField(null=True, blank=True)

    class Meta:
        app_label = 'data'

    def __str__(self):
        return str(self.user)
