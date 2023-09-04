from django import forms
from .models import Comment_6, Write_6

class WriteForm_6(forms.ModelForm):
    class Meta:
        model = Write_6
        fields = ('제목', '내용', '사진')

class Commentform_6(forms.ModelForm):
    class Meta:
        model = Comment_6
        fields = ('댓글',)