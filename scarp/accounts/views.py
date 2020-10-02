from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from .forms import CreateUserForm

from django.views.generic import CreateView
# from .models import Person

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form':form}
    return render(request, 'registration/registration.html', context)

# def registration(request):
#     success_url = reverse_lazy('login')
#     return render(request, 'templates/registration/registration.html')

# class PersonCreateView(CreateView):
#     model = Person
#     fields = ('ФИ', 'email', 'Класс', 'Пароль')
#     template_name = 'registration/signup.html'
#     success_url = reverse_lazy('login')