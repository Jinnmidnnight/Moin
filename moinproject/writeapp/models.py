from django.db import models
from django.db.models.fields import CharField, TextField
from django.utils import timezone
from openapp.models import Open_1, Open_2, Open_3, Open_4, Open_5, Open_6, Open_7, Open_8, Open_9

# Create your models here.
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

class Write_2(models.Model):
    post = models.ForeignKey(Open_2, related_name = 'writes', on_delete = models.CASCADE, null = True)
    제목 = models.CharField(max_length=200)
    내용 = models.TextField()
    사진 = models.ImageField(upload_to = "Write_2", null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save()

    def __str__(self):
        return self.작성자

class Write_3(models.Model):
    post = models.ForeignKey(Open_3, related_name = 'writes', on_delete = models.CASCADE, null = True)
    제목 = models.CharField(max_length=200)
    내용 = models.TextField()
    사진 = models.ImageField(upload_to = "Write_3", null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save()

    def __str__(self):
        return self.작성자
    
class Write_4(models.Model):
    post = models.ForeignKey(Open_4, related_name = 'writes', on_delete = models.CASCADE, null = True)
    제목 = models.CharField(max_length=200)
    내용 = models.TextField()
    사진 = models.ImageField(upload_to = "Write_4", null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save()

    def __str__(self):
        return self.작성자

class Write_5(models.Model):
    post = models.ForeignKey(Open_5, related_name = 'writes', on_delete = models.CASCADE, null = True)
    제목 = models.CharField(max_length=200)
    내용 = models.TextField()
    사진 = models.ImageField(upload_to = "Write_5", null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save()

    def __str__(self):
        return self.작성자

class Write_6(models.Model):
    post = models.ForeignKey(Open_6, related_name = 'writes', on_delete = models.CASCADE, null = True)
    제목 = models.CharField(max_length=200)
    내용 = models.TextField()
    사진 = models.ImageField(upload_to = "Write_6", null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save()

    def __str__(self):
        return self.작성자

class Write_7(models.Model):
    post = models.ForeignKey(Open_7, related_name = 'writes', on_delete = models.CASCADE, null = True)
    제목 = models.CharField(max_length=200)
    내용 = models.TextField()
    사진 = models.ImageField(upload_to = "Write_7", null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save()

    def __str__(self):
        return self.작성자

class Write_8(models.Model):
    post = models.ForeignKey(Open_8, related_name = 'writes', on_delete = models.CASCADE, null = True)
    제목 = models.CharField(max_length=200)
    내용 = models.TextField()
    사진 = models.ImageField(upload_to = "Write_8", null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save()

    def __str__(self):
        return self.작성자

class Write_9(models.Model):
    post = models.ForeignKey(Open_9, related_name = 'writes', on_delete = models.CASCADE, null = True)
    제목 = models.CharField(max_length=200)
    내용 = models.TextField()
    사진 = models.ImageField(upload_to = "Write_9", null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save()

    def __str__(self):
        return self.작성자

class Comment_1(models.Model):
    post = models.ForeignKey(Write_1, related_name = 'comments', on_delete = models.CASCADE, null = True)
    댓글 = models.CharField(max_length = 200)
    created_at = models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save()
    
    def __str__(self):
        return self.작성자

class Comment_2(models.Model):
    post = models.ForeignKey(Write_2, related_name = 'comments', on_delete = models.CASCADE, null = True)
    댓글 = models.CharField(max_length = 200)
    created_at = models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save()
    
    def __str__(self):
        return self.작성자

class Comment_3(models.Model):
    post = models.ForeignKey(Write_3, related_name = 'comments', on_delete = models.CASCADE, null = True)
    댓글 = models.CharField(max_length = 200)
    created_at = models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save()
    
    def __str__(self):
        return self.작성자

class Comment_4(models.Model):
    post = models.ForeignKey(Write_4, related_name = 'comments', on_delete = models.CASCADE, null = True)
    댓글 = models.CharField(max_length = 200)
    created_at = models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save()
    
    def __str__(self):
        return self.작성자

class Comment_5(models.Model):
    post = models.ForeignKey(Write_5, related_name = 'comments', on_delete = models.CASCADE, null = True)
    댓글 = models.CharField(max_length = 200)
    created_at = models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save()
    
    def __str__(self):
        return self.작성자

class Comment_6(models.Model):
    post = models.ForeignKey(Write_6, related_name = 'comments', on_delete = models.CASCADE, null = True)
    댓글 = models.CharField(max_length = 200)
    created_at = models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save()
    
    def __str__(self):
        return self.작성자

class Comment_7(models.Model):
    post = models.ForeignKey(Write_7, related_name = 'comments', on_delete = models.CASCADE, null = True)
    댓글 = models.CharField(max_length = 200)
    created_at = models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save()
    
    def __str__(self):
        return self.작성자

class Comment_8(models.Model):
    post = models.ForeignKey(Write_8, related_name = 'comments', on_delete = models.CASCADE, null = True)
    댓글 = models.CharField(max_length = 200)
    created_at = models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save()
    
    def __str__(self):
        return self.작성자

class Comment_9(models.Model):
    post = models.ForeignKey(Write_9, related_name = 'comments', on_delete = models.CASCADE, null = True)
    댓글 = models.CharField(max_length = 200)
    created_at = models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save()
    
    def __str__(self):
        return self.작성자