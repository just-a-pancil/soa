from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import GradeForm


def choose_class_please(request):
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('choose_class_please')
    
    return render(request, 'profile.html')
