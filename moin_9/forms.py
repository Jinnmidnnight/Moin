from django import forms
from .models import Comment_9, Write_9

class WriteForm_9(forms.ModelForm):
    class Meta:
        model = Write_9
        fields = ('제목', '내용', '사진')

class Commentform_9(forms.ModelForm):
    class Meta:
        model = Comment_9
        fields = ('댓글',)