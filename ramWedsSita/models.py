from django.db import models

# Create your models here.
class Wisher(models.Model):
    name= models.CharField(max_length=20)
    wishes = models.CharField(max_length=500)
    posted = models.DateTimeField(auto_now=True)

