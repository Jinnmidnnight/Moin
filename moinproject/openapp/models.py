from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from account.models import User
from django.conf import settings

# Create your models here.



class Open_1(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='작성자')
    title = models.CharField(max_length=200)
    intro = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to = "Open_1", null=True, blank=True)
    number = models.IntegerField(default=0, validators = [MinValueValidator(0), MaxValueValidator(50)], null=True, blank=True)
    
    like = models.ManyToManyField(User, related_name='likes_1', blank=True)
    like_count = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title

class Open_2(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='작성자')
    title = models.CharField(max_length=200)
    intro = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to = "Open_2", null=True, blank=True)
    number = models.IntegerField(default=0, validators = [MinValueValidator(0), MaxValueValidator(50)], null=True, blank=True)

    like = models.ManyToManyField(User, related_name='likes_2', blank=True)
    like_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class Open_3(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='작성자')
    title = models.CharField(max_length=200)
    intro = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to = "Open_3", null=True, blank=True)
    number = models.IntegerField(default=0, validators = [MinValueValidator(0), MaxValueValidator(50)], null=True, blank=True)

    like = models.ManyToManyField(User, related_name='likes_3', blank=True)
    like_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class Open_4(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='작성자')
    title = models.CharField(max_length=200)
    intro = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to = "Open_4", null=True, blank=True)
    number = models.IntegerField(default=0, validators = [MinValueValidator(0), MaxValueValidator(50)], null=True, blank=True)

    like = models.ManyToManyField(User, related_name='likes_4', blank=True)
    like_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class Open_5(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='작성자')
    title = models.CharField(max_length=200)
    intro = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to = "Open_5", null=True, blank=True)
    number = models.IntegerField(default=0, validators = [MinValueValidator(0), MaxValueValidator(50)], null=True, blank=True)

    like = models.ManyToManyField(User, related_name='likes_5', blank=True)
    like_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class Open_6(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='작성자')
    title = models.CharField(max_length=200)
    intro = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to = "Open_6", null=True, blank=True)
    number = models.IntegerField(default=0, validators = [MinValueValidator(0), MaxValueValidator(50)], null=True, blank=True)

    like = models.ManyToManyField(User, related_name='likes_6', blank=True)
    like_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class Open_7(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='작성자')
    title = models.CharField(max_length=200)
    intro = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to = "Open_7", null=True, blank=True)
    number = models.IntegerField(default=0, validators = [MinValueValidator(0), MaxValueValidator(50)], null=True, blank=True)

    like = models.ManyToManyField(User, related_name='likes_7', blank=True)
    like_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class Open_8(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='작성자')
    title = models.CharField(max_length=200)
    intro = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to = "Open_8", null=True, blank=True)
    number = models.IntegerField(default=0, validators = [MinValueValidator(0), MaxValueValidator(50)], null=True, blank=True)

    like = models.ManyToManyField(User, related_name='likes_8', blank=True)
    like_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class Open_9(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='작성자')
    title = models.CharField(max_length=200)
    intro = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to = "Open_9", null=True, blank=True)
    number = models.IntegerField(default=0, validators = [MinValueValidator(0), MaxValueValidator(50)], null=True, blank=True)

    like = models.ManyToManyField(User, related_name='likes_9', blank=True)
    like_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
