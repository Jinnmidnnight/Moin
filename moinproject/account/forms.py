from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', '이름', '성별', '생년월일']
        #fields = ['username', 'password1', 'password2', '닉네임', '나이', '성별', '직업', '연애횟수']