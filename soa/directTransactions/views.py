from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.defaults import page_not_found
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from .models import Coins


# class DirectTransactions:
    
#     def __init__(self, amount=0, user_id=None):
#         self.amount = amount
#         self.user_id = user_id

#     def is_teacher(self.user):
#         return user.groups.filter(name='Teacher').exists()

#     def direct_transaction_add( amount, user_id):
#         coin_profile = Coins.objects.get(user_id=user_id)
#         coin_profile.coins += amount
#         coin_profile.save()
#         return True

#     @login_required
#     def directTransaction(request, user_id, amount):
#         # is user teacher?
#         user = User.objects.get(username=request.user)
#         if is_teacher(user):
#             if direct_transaction_add(amount, user_id=user_id): 
#                 return redirect('profile')  
#         return render(request, 'base.html')




# def directTransaction(amount, user_id):
    

def is_teacher(user):
    return user.groups.filter(name='Teacher').exists()

def direct_transaction_add( amount, user_id):
    coin_profile = Coins.objects.get(user_id=user_id)
    coin_profile.coins += amount
    coin_profile.save()
    return True

@login_required
def directTransaction(request, user, amount):
    if direct_transaction_add(amount, user_id=user.id): 
        return True
    return False

def directTransactionForTeacher(request, user_id, amount):
    # is user teacher?
    user = User.objects.get(username=request.user)
    user_accept_to = User.objects.get(id=user_id)
    if is_teacher(user): 
        return directTransaction(request, user_accept_to, amount)
