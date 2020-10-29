from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def lists(request):
    return render(request, 'lists.html')

def create_list(request):
    pass