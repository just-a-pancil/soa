from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.defaults import page_not_found
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from directTransactions.models import Coins
from newKey.models import Keys
import qrcode


def is_teacher(user):
    return user.groups.filter(name='Teacher').exists()

@login_required
def showQr(request, token):
    # is user teacher?
    user = User.objects.get(username=request.user)
    if is_teacher(user):        
        return render(request, 'show_qr.html', {'token':token})
    return render(request, 'base.html')
