from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Нужен для восстановления пароля')
    first_name = forms.CharField(max_length=20,label='Имя')
    last_name = forms.CharField(max_length=20,label='Фамилия')
    username = forms.CharField(max_length=20,help_text='''Только буквы, цифры и символы @/./+/-/_.''',label='Имя пользователя')
    teacherCheck = forms.BooleanField(initial = True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', "email", "password1", "password2"]
