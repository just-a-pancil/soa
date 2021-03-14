from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from . import forms
import importlib
from django import forms as djangoforms


# @login_required
def classChoose(request):
    context = {}
    try:
        # ooohhhh
        importlib.reload(forms)
        grades = forms.classChooseForm.GRADES_CHOICES
        form = 123
        form = forms.classChooseForm()
        context = {'form':form}
        user = User.objects.get(username=request.user)
        print('[DEBUG]:' +'\n'.join(map(str,form.GRADES_CHOICES)))
        

        if request.method == 'POST':
            chosen_class = int(request.POST.get('chosen_class'))
            chosen_class = grades[chosen_class]
            print(chosen_class)
            form = forms.classChooseForm(request.POST)
            if form.is_valid():
                if chosen_class == grades[0]: 
                    return render(request, 'class_choose.html', context)
                elif chosen_class == grades[-1]:
                    group_name = request.POST.get('your_variant')
                    (group, created) = Group.objects.get_or_create(name=group_name)
                    user.groups.add(group)
                    return redirect('http://127.0.0.1:8000/profile/')
                    # form.fields['your_variant'].disabled = False
                    # context = {'form':form}
                    # return render(request, 'class_choose.html', context)
                    # return redirect('classChoose')
                else:
                    group_name = chosen_class[1]
                    user.groups.add(Group.objects.get(name=group_name))
                    return redirect('classChoose')
    except User.DoesNotExist as e:
        context['errmsg'] = e
        context['errtype'] = type(e)
    # finally:
    #     return render(request, 'errors/common.html', context)
    return render(request, 'class_choose.html', context)
    # return render(request, 'errors/common.html')