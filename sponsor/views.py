from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import *
from ideapeacher.forms import CreateUserForm
from ideapeacher.decorators import *
from .models import *
from django.db.models import Q

# Create your views here.
#register the new user and create the group if not or keep the user in the old group
@unauthenticated_user
def registersponsor(request):
    form = CreateUserForm()
    if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                
                if not  Group.objects.filter(name='sponsor').exists():
                    group = Group.objects.create(name='sponsor')
                    addtogroup =  Group.objects.get(name='sponsor')
                    user.groups.add(addtogroup)
                    sponsor.objects.create(user=user,name=user.username)
                    messages.success(request, 'Account was created for ' + username)

                    return redirect('home')
                else:
                    group = Group.objects.get(name='sponsor')
                    user.groups.add(group)
                    sponsor.objects.create(user=user,name=user.username)
                    messages.success(request, 'Account was created for ' + username)
                    return redirect('home')


    context = {'form': form}
    return render(request, 'main/register1.html', context)

