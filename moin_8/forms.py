from django import forms
from .models import Comment_8, Write_8

class WriteForm_8(forms.ModelForm):
    class Meta:
        model = Write_8
        fields = ('제목', '내용', '사진')

class Commentform_8(forms.ModelForm):
    class Meta:
        model = Comment_8
        fields = ('댓글',)