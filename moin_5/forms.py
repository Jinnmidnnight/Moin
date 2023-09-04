from django import forms
from .models import Comment_5, Write_5

class WriteForm_5(forms.ModelForm):
    class Meta:
        model = Write_5
        fields = ('제목', '내용', '사진')

class Commentform_5(forms.ModelForm):
    class Meta:
        model = Comment_5
        fields = ('댓글',)