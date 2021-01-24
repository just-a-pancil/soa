from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django_email_verification import sendConfirm
from django.contrib.auth.models import User

from .forms import CreateUserForm
from .forms import GradeForm    

def setGrade(request):
    gradeForm = GradeForm
    context = {'form':gradeForm}
    return render(request, "choose_class_please.html", context)


def confirmEmail(user):
    sendConfirm(user)
    return 0




def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.get(username=request.POST['username'])
            if confirmEmail(user) != 0:
                print("%s: confirmEmail func is fallen" %('[DEBUG]'))
            return redirect('conformition')

    context = {'form':form}
    return render(request, 'registration/signup.html', context)

# problem: rewrite conformition function
    
def conformition(request):
    return render(request, 'registration/confirm_signup.html')