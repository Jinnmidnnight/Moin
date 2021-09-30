from django import forms
from .models import Write_1, Write_2, Write_3, Write_4, Write_5, Write_6, Write_7, Write_8, Write_9

class WriteForm_1(forms.ModelForm):
    class Meta:
        model = Write_1
        fields = ('제목', '내용', '사진')

class WriteForm_2(forms.ModelForm):
    class Meta:
        model = Write_2
        fields = ('제목', '내용', '사진')

class WriteForm_3(forms.ModelForm):
    class Meta:
        model = Write_3
        fields = ('제목', '내용', '사진')

class WriteForm_4(forms.ModelForm):
    class Meta:
        model = Write_4
        fields = ('제목', '내용', '사진')

class WriteForm_5(forms.ModelForm):
    class Meta:
        model = Write_5
        fields = ('제목', '내용', '사진')

class WriteForm_6(forms.ModelForm):
    class Meta:
        model = Write_6
        fields = ('제목', '내용', '사진')

class WriteForm_7(forms.ModelForm):
    class Meta:
        model = Write_7
        fields = ('제목', '내용', '사진')

class WriteForm_8(forms.ModelForm):
    class Meta:
        model = Write_8
        fields = ('제목', '내용', '사진')

class WriteForm_9(forms.ModelForm):
    class Meta:
        model = Write_9
        fields = ('제목', '내용', '사진')