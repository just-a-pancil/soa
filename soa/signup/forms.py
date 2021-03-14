from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='''Нужен для активации аккаунта и восстановления пароля. Укажите тот, к которому у вас есть доступ прямо сейчас''')
    first_name = forms.CharField(max_length=20,label='Имя')
    last_name = forms.CharField(max_length=20,label='Фамилия')
    username = forms.CharField(max_length=40,help_text='''Ваш логин. Удобно использовать почту''',label='Имя пользователя')
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', "email", "password1", "password2"]
