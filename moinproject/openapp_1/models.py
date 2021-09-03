from django.db import models
from django.db.models.fields import CharField, TextField
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Open_1(models.Model):
    title = models.CharField(max_length=200)
    intro = models.CharField(max_length=200)
    conent = models.TextField()
    image = models.ImageField(upload_to = "openapp_1", null=True, blank=True)
    number = models.IntegerField(validators = [MinValueValidator(0), MaxValueValidator(50)], null=True, blank=True)