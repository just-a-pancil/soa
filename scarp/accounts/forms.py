from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        # fields = ['FName', "SName", "Nick", "Email", "Pass1", "Pass2"]
        fields = ['first_name', 'last_name', 'username', "email", "password1", "password2"]
