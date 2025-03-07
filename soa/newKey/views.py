from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.defaults import page_not_found
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from directTransactions.models import Coins
from .models import Keys
import qrcode

from newKey.models import Keys



def is_teacher(user):
    return user.groups.filter(name='Teacher').exists()

def generate_group():
    pass

@login_required
def generate_key(request):
    # is user teacher?
    user = User.objects.get(username=request.user)
    if is_teacher(user):
        if request.method == "GET":
            # getting parametres
            amount = request.GET.get('amount')
            life = request.GET.get('life')
            key = Keys.create(request, amount, life)

        elif request.method == 'POST':
            errmsg = 'newKey.views got POST request'
            return render(request, 'errors/common.html', {'errmsg':errmsg})


        return redirect('http://127.0.0.1:8000/show-qr/'+key.token)  
    return render(request, 'base.html')