from django import forms
from .models import Comment_2, Write_2

class WriteForm_2(forms.ModelForm):
    class Meta:
        model = Write_2
        fields = ('제목', '내용', '사진')

class Commentform_2(forms.ModelForm):
    class Meta:
        model = Comment_2
        fields = ('댓글',)