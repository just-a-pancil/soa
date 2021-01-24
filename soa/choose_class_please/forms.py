from django.forms import ModelForm
from django import forms
from profiles.models import Lists

class GradeForm(forms.ModelForm):
    lists = forms.CharField(max_length=3, label='Класс' ) 
