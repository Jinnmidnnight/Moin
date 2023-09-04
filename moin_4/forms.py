from django import forms
from .models import Comment_4, Write_4

class WriteForm_4(forms.ModelForm):
    class Meta:
        model = Write_4
        fields = ('제목', '내용', '사진')

class Commentform_4(forms.ModelForm):
    class Meta:
        model = Comment_4
        fields = ('댓글',)