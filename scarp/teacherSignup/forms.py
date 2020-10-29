from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from .models import Teacher

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Нужен для восстановления пароля')
    first_name = forms.CharField(max_length=20,label='Имя')
    last_name = forms.CharField(max_length=20,label='Фамилия')
    username = forms.CharField(max_length=20,help_text='''Ваш логин. Удобно использовать почту''',label='Имя пользователя')
    teacherCheck = forms.BooleanField(initial = True, label='Я учитель')
    class Meta:
        model = User
        fields = [ "teacherCheck", 'username', 'first_name', 'last_name', "email", "password1", "password2",]
