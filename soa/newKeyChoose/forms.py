from django.forms import ModelForm
from django import forms
import django.forms.widgets
from django.core.validators import MinValueValidator

class GenerateKeyForm(forms.Form):
    duration_minutes = forms.IntegerField(
        widget=forms.NumberInput(attrs={'step':1,'min':0}),
        initial=0,
        label='',
        help_text='Минут',
        )
    duration_hours = forms.IntegerField(
        widget=forms.NumberInput(attrs={'step':1,'min':0}),
        initial=1,
        label='',
        help_text='Часов',
        )
    duration_days = forms.IntegerField(
        widget=forms.NumberInput(attrs={'step':1,'min':0}),
        initial=0,
        label='',
        help_text='Дней',
        )
        
    scan_amount = forms.IntegerField(
        widget=forms.NumberInput(attrs={'step':1,'min':0}),
        initial=0,
        label='Ссылка будет действительна абракадавра',
        )
        
    amount = forms.IntegerField(
            widget=forms.NumberInput(attrs={'step':1,'min':0}),
            initial=0,
            label='Ученики получат по ',
            help_text='баллов',
            )
        
