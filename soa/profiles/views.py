from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required


def ShowProfle(request):
    context = {}
    # print(repr(request.GET.get('amount')))
    try:
        # print(request.__dir__())
        user = User.objects.get(username=request.user)
        # if not user.last_login:
        context['msg'] = 'Profile successfully disabled.'
    except Exception as e:
        context['msg'] = e
    return render(request, 'profile.html', context)

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
