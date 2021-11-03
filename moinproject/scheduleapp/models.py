from django.db import models

# Create your models here.

class Schedule_1(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(null=True)
    location = models.CharField(max_length=300)
    price = models.CharField(max_length=200)