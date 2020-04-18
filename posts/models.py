from django.db import models
from data.models import Club

# Create your models here.

class Posts(models.Model):
    name = models.CharField(max_length=100, default="user")
    value = models.CharField(max_length=100)
    team = models.ForeignKey(Club, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    class Meta :
        app_label = "posts"
