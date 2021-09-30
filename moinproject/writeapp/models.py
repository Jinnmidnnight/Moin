from django.db import models
from django.db.models.fields import CharField, TextField
from django.utils import timezone
from openapp.models import Open_1

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
