from django.forms import ModelForm
from django import forms
import django.forms.widgets
from django.core.validators import MinValueValidator
from django.contrib.auth.models import Group


class classChooseForm(forms.Form):

    grades = Group.objects.filter(name__iregex=r'класс|grade').order_by('name')
    first_item = list(Group.objects.get_or_create(name='Выберете клаcc из списка'))
    first_item.pop()
    grades = (
        first_item + list(grades)
        )
    GRADES_CHOICES = [
        tuple([count, grade]) 
        for count, grade in enumerate(grades)
                        ] 

    GRADES_CHOICES += [(GRADES_CHOICES[-1][0]+1, 'свой вариант')]


    # you can't enter something here, you can only choose smth
    chosen_class = forms.ChoiceField(
        choices=GRADES_CHOICES,
        label="Пожалуйста, укажите свой класс",
        # widget=forms.Select(choices=GRADES_CHOICES),
        help_text="Если вашего класса нет в списке, впишите его в поле ниже, предварительно выбрав 'свой вариант' в первом поле"
        )

    # here you can enter what you want 
    your_variant = forms.CharField(
        # widget=forms.NumberInput(attrs={'step':1,'min':0}),
        max_length=40,
        initial='',
        label='Свой вариант',
        help_text='',
        required=False,
        )