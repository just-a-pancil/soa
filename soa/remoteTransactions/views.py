from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.defaults import page_not_found
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from directTransactions.models import Coins
from newKey.models import Keys
from directTransactions.views import  directTransaction


def is_key_exists(token):

    if Keys.objects.filter(token = token) and Group.object.filter(name='key'+token):
        return True
    return False


def first_scan(user, token, ):
    # yes, this is "__" in "name__in" filter
    return not user.groups.filter(name__in=['key_'+token]).exists()

@login_required
def remoteTransaction(request, token):
    user = User.objects.get(username=request.user)

    # is token exists
    if not is_key_exists(token):
        errmsg = 'Неверный код/ссылка'
        return render(request, 'errors/common.html', {'errmsg': errmsg})

    if not first_scan(user,token):
        #something went wrong
        errmsg = 'Вы уже сканировали этот код'
        return render(request, 'errors/common.html', {'errmsg': errmsg})

    user.groups.add(Group.objects.get(name='key_'+token))
    key = Keys.objects.get(token = token)
    
    # is key valid?
    if key.is_valid():
        if directTransaction(request, user, key.amount):
            return redirect('profile')
    # if key isn't valid
    else:
        errmsg = ''
        if not key.is_valid_by_date:
            errmsg += 'ссылка/код недействительны'
        if not key.is_valid_by_scan_amount:
            errmsg += 'превышено количество сканирований одного кода'
            return render(request, 'errors/common.html', {
                'errmsg':errmsg})


