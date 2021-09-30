from django import forms
from .models import Comment_1, Write_1, Write_2, Write_3, Write_4, Write_5, Write_6, Write_7, Write_8, Write_9, Comment_1, Comment_2, Comment_3, Comment_4, Comment_5, Comment_6, Comment_7, Comment_8, Comment_9

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

class Commentform_1(forms.ModelForm):
    class Meta:
        model = Comment_1
        fields = ('댓글',)

class Commentform_2(forms.ModelForm):
    class Meta:
        model = Comment_2
        fields = ('댓글',)

class Commentform_3(forms.ModelForm):
    class Meta:
        model = Comment_3
        fields = ('댓글',)

class Commentform_4(forms.ModelForm):
    class Meta:
        model = Comment_4
        fields = ('댓글',)

class Commentform_5(forms.ModelForm):
    class Meta:
        model = Comment_5
        fields = ('댓글',)

class Commentform_6(forms.ModelForm):
    class Meta:
        model = Comment_6
        fields = ('댓글',)

class Commentform_7(forms.ModelForm):
    class Meta:
        model = Comment_7
        fields = ('댓글',)

class Commentform_8(forms.ModelForm):
    class Meta:
        model = Comment_8
        fields = ('댓글',)

class Commentform_9(forms.ModelForm):
    class Meta:
        model = Comment_9
        fields = ('댓글',)