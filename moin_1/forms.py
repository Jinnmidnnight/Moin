from django import forms
from .models import Comment_1, Write_1

class WriteForm_1(forms.ModelForm):
    class Meta:
        model = Write_1
        fields = ('제목', '내용', '사진')

class Commentform_1(forms.ModelForm):
    class Meta:
        model = Comment_1
        fields = ('댓글',)