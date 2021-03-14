from django.shortcuts import render, redirect
from django.views.defaults import page_not_found
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from django import forms
import django.forms.widgets
from .forms import GenerateKeyForm
from urllib.parse import urlencode



def generate_key(request):
    form = GenerateKeyForm()
    if request.method == 'POST':
        form = GenerateKeyForm(request.POST)
        print(request.content_params)
        print(request.body)
        print(request.path)
        if form.is_valid():
            post = request.POST
            dur_min = int(post.get('duration_minutes'))
            dur_hrs = int(post.get('duration_hours'))
            dur_dys = int(post.get('duration_days'))
            amount = post.get('amount')
            life = dur_min + dur_hrs*60 + dur_dys*24*60
            link = ("http://127.0.0.1:8000/generate-key/?" 
            + 'life='+str(life))
            if amount != '0': link += "&amount="+amount
            print(link)
            return redirect(link)

    context = {'form':form}
    return render(request, 'generate_key_page.html', context)

