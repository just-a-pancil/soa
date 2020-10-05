from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from .forms import CreateUserForm

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    
    context = {'form':form}
    return render(request, 'registration/signup.html', context)
    # return render(request, 'registration/signup.html')

# def registration(request):
#     success_url = reverse_lazy('login')
#     return render(request, 'templates/registration/registration.html')
