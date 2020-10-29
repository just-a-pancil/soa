from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required

def profile(request):
    return render(request, 'profile.html')

# @login_required
# def delete_user(request, username):
#     context = {}
#     if 
#     try:
#         user = User.object.get(username=username)
#         user.is_active = False
#         user.save()
#         context['msg'] = 'Profile successfully disabled.'
#     except User.DoesNotExist:
#         context['msg'] = 'User does not exist.'
#     except Exception as e:
#         context['msg'] = e.message

#     return render(request, 'template.html', context=context) 
