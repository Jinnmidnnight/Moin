from django.db import models
from django.db.models.fields import CharField, TextField
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Open_1(models.Model):
    title = models.CharField(max_length=200)
    intro = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to = "openapp_1", null=True, blank=True)
    number = models.IntegerField(default=0, validators = [MinValueValidator(0), MaxValueValidator(50)], null=True, blank=True)

class Open_2(models.Model):
    title = models.CharField(max_length=200)
    intro = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to = "openapp_1", null=True, blank=True)
    number = models.IntegerField(default=0, validators = [MinValueValidator(0), MaxValueValidator(50)], null=True, blank=True)

class Open_3(models.Model):
    title = models.CharField(max_length=200)
    intro = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to = "openapp_1", null=True, blank=True)
    number = models.IntegerField(default=0, validators = [MinValueValidator(0), MaxValueValidator(50)], null=True, blank=True)

class Open_4(models.Model):
    title = models.CharField(max_length=200)
    intro = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to = "openapp_1", null=True, blank=True)
    number = models.IntegerField(default=0, validators = [MinValueValidator(0), MaxValueValidator(50)], null=True, blank=True)

class Open_5(models.Model):
    title = models.CharField(max_length=200)
    intro = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to = "openapp_1", null=True, blank=True)
    number = models.IntegerField(default=0, validators = [MinValueValidator(0), MaxValueValidator(50)], null=True, blank=True)

class Open_6(models.Model):
    title = models.CharField(max_length=200)
    intro = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to = "openapp_1", null=True, blank=True)
    number = models.IntegerField(default=0, validators = [MinValueValidator(0), MaxValueValidator(50)], null=True, blank=True)

class Open_7(models.Model):
    title = models.CharField(max_length=200)
    intro = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to = "openapp_1", null=True, blank=True)
    number = models.IntegerField(default=0, validators = [MinValueValidator(0), MaxValueValidator(50)], null=True, blank=True)

class Open_8(models.Model):
    title = models.CharField(max_length=200)
    intro = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to = "openapp_1", null=True, blank=True)
    number = models.IntegerField(default=0, validators = [MinValueValidator(0), MaxValueValidator(50)], null=True, blank=True)

class Open_9(models.Model):
    title = models.CharField(max_length=200)
    intro = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to = "openapp_1", null=True, blank=True)
    number = models.IntegerField(default=0, validators = [MinValueValidator(0), MaxValueValidator(50)], null=True, blank=True)
