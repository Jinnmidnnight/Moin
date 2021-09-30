from django.db import models
from django.db.models.fields import CharField, TextField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

# Create your models here.

class Open_1(models.Model):
    title = models.CharField(max_length=200)
    intro = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to = "Open_1", null=True, blank=True)
    number = models.IntegerField(default=0, validators = [MinValueValidator(0), MaxValueValidator(50)], null=True, blank=True)

class Open_2(models.Model):
    title = models.CharField(max_length=200)
    intro = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to = "Open_2", null=True, blank=True)
    number = models.IntegerField(default=0, validators = [MinValueValidator(0), MaxValueValidator(50)], null=True, blank=True)

class Open_3(models.Model):
    title = models.CharField(max_length=200)
    intro = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to = "Open_3", null=True, blank=True)
    number = models.IntegerField(default=0, validators = [MinValueValidator(0), MaxValueValidator(50)], null=True, blank=True)

class Open_4(models.Model):
    title = models.CharField(max_length=200)
    intro = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to = "Open_4", null=True, blank=True)
    number = models.IntegerField(default=0, validators = [MinValueValidator(0), MaxValueValidator(50)], null=True, blank=True)

class Open_5(models.Model):
    title = models.CharField(max_length=200)
    intro = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to = "Open_5", null=True, blank=True)
    number = models.IntegerField(default=0, validators = [MinValueValidator(0), MaxValueValidator(50)], null=True, blank=True)

class Open_6(models.Model):
    title = models.CharField(max_length=200)
    intro = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to = "Open_6", null=True, blank=True)
    number = models.IntegerField(default=0, validators = [MinValueValidator(0), MaxValueValidator(50)], null=True, blank=True)

class Open_7(models.Model):
    title = models.CharField(max_length=200)
    intro = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to = "Open_7", null=True, blank=True)
    number = models.IntegerField(default=0, validators = [MinValueValidator(0), MaxValueValidator(50)], null=True, blank=True)

class Open_8(models.Model):
    title = models.CharField(max_length=200)
    intro = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to = "Open_8", null=True, blank=True)
    number = models.IntegerField(default=0, validators = [MinValueValidator(0), MaxValueValidator(50)], null=True, blank=True)

class Open_9(models.Model):
    title = models.CharField(max_length=200)
    intro = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to = "Open_9", null=True, blank=True)
    number = models.IntegerField(default=0, validators = [MinValueValidator(0), MaxValueValidator(50)], null=True, blank=True)

class Write_1(models.Model):
    post = models.ForeignKey(Open_1, related_name = 'writes', on_delete = models.CASCADE, null = True)
    제목 = models.CharField(max_length=200)
    내용 = models.TextField()
    사진 = models.ImageField(upload_to = "Write_1", null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save()

    def __str__(self):
        return self.작성자
