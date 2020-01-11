from django.shortcuts import render, redirect 
from .forms import NewForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import idea 



# Create your views here.
def homepage(request):
    return render(request,"main/home.html", context={"idea":idea.objects.all})


def register(request):
    if request.method == "POST":
        form = NewForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/home")
    else:
        form = NewForm()
    return render (request, "main/register.html",{"form":form})


def logout_request(request):
    logout(request)
    return redirect("/home")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST )
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request , user)
                return redirect("/home")
            else:
                messages.error (request, "Invalid username or password")
    
    form = AuthenticationForm()
    return render (request, "main/login.html", {"form":form})
    

