from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):

    GENDER_CHOICES = (
        (0, '남성'),
        (1, '여성')
    )

    성별 = models.SmallIntegerField(choices = GENDER_CHOICES, null=True)

    생년월일 = models.DateField(null=True)

    자기소개 = models.TextField(null=True)

    image = models.ImageField(blank = True)