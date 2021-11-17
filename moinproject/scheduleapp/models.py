from django.db import models
from openapp.models import Open_1, Open_2, Open_3, Open_4, Open_5, Open_6, Open_7, Open_8, Open_9
from django.conf import settings

# Create your models here.

class Schedule_1(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='작성자')
    title = models.CharField(max_length=200)
    date = models.DateField(null=True)
    location = models.CharField(max_length=300)
    price = models.CharField(max_length=200)

    def __str__(self):
        return self.title