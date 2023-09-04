from django.db import models
from django.db.models.fields import CharField, TextField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from account.models import User
from django.conf import settings

class Open_1(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='작성자')
    title = models.CharField(max_length=200)
    intro = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to = "Open_1", null=True, blank=True)
    number = models.IntegerField(default=0, validators = [MinValueValidator(0), MaxValueValidator(50)], null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    like = models.ManyToManyField(User, related_name='likes_1', blank=True)
    like_count = models.PositiveIntegerField(default=0)

    follower  = models.ManyToManyField(User, related_name='followers', blank=True, null=True)
    follower_count = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return self.title

class Write_1(models.Model):
    post = models.ForeignKey(Open_1, related_name = 'writes', on_delete = models.CASCADE, null = True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='사람')
    제목 = models.CharField(max_length=200)
    내용 = models.TextField()
    사진 = models.ImageField(upload_to = "Write_1", null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    write_like = models.ManyToManyField(User, related_name='write_likes_1', blank=True)
    write_like_count = models.PositiveIntegerField(default=0)
    comment_count = models.PositiveIntegerField(default=0)

    def approve(self):
        self.save()

    def __str__(self):
        return self.작성자

class Comment_1(models.Model):
    post = models.ForeignKey(Write_1, related_name = 'comments', on_delete = models.CASCADE, null = True)
    댓글 = models.CharField(max_length = 200)
    created_at = models.DateTimeField(default=timezone.now)
    reply = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='답변')

    def approve(self):
        self.save()
    
    def __str__(self):
        return self.작성자

