from django import forms
from .models import Comment_3, Write_3

class WriteForm_3(forms.ModelForm):
    class Meta:
        model = Write_3
        fields = ('제목', '내용', '사진')

class Commentform_3(forms.ModelForm):
    class Meta:
        model = Comment_3
        fields = ('댓글',)