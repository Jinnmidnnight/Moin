from django import forms
from .models import Comment_7, Write_7

class WriteForm_7(forms.ModelForm):
    class Meta:
        model = Write_7
        fields = ('제목', '내용', '사진')

class Commentform_7(forms.ModelForm):
    class Meta:
        model = Comment_7
        fields = ('댓글',)