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
from .forms import CreateUserForm
from .decorators import *
from .models import *
from django.db.models import Q


# Create your views here.

# register the new user and create the group if not or keep the user in the old group
@unauthenticated_user
def registerpeacher(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            if not Group.objects.filter(name='ideapeacher').exists():
                group = Group.objects.create(name='ideapeacher')
                addtogroup = Group.objects.get(name='ideapeacher')
                user.groups.add(addtogroup)
                ideapeacher.objects.create(user=user, name=user.username)
                messages.success(
                    request, 'Account was created for ' + username)

                return redirect('home')
            else:
                group = Group.objects.get(name='ideapeacher')
                user.groups.add(group)
                ideapeacher.objects.create(user=user, name=user.username)
                messages.success(
                    request, 'Account was created for ' + username)
                return redirect('home')

    context = {'form': form}
    return render(request, 'main/register.html', context)

# check the user is register or not while login


@unauthenticated_user
def login_request(request):

    if request.method == 'POST':
        # get username value from input field
        username = request.POST.get('username')
        # get password value from input field
        password = request.POST.get('password')

        # check the username and password in database
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'main/login.html', context)

# logout request


def logout_request(request):
    logout(request)
    return redirect('/')

# if user is ideapeacher send to ideapeacher page


@login_required(login_url='login')
@ideapaeacher_only  # define in decorator only access to ideapeacher define in group
def ideapeacherpage(request):

    i = idea.objects.all()
    b = Public.objects.all()
    query = ""
    if request.GET:
        query = request.GET['q']
        i = get_data_queryset(str(query))

    return render(request, "main/home.html", context={"ideas": i, "comments": b})

# if user is sponsor send him to sponsor page


@login_required(login_url='login')
# define in decorator, only access to sponsor define in group
@allowed_users(allowed_roles=['sponsor'])
def sponsorpage(request):
    u = ideapeacher.objects.all()
    i = idea.objects.all()
    b = Public.objects.all()
    query = ""
    if request.GET:
        query = request.GET['q']
        i = get_data_queryset(str(query))

    return render(request, "main/home1.html", context={"ideas": i, "comments": b, "users": u})

# search functionality


def get_data_queryset(query):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        u = ideapeacher.objects.filter(name__icontains=q)
        ideas = idea.objects.filter(
            Q(peacher__in=u)).distinct()

        for i in ideas:
            queryset.append(i)
    return list(set(queryset))

# this views allow ideapeacher only to submit their idea


@login_required(login_url='login')
@allowed_users(allowed_roles=['ideapeacher'])
def submitidea(request):
    if request.method == "POST":
        c = request.POST.get("dropdown")
        # if category dosenot exist in the database add to database
        if not category.objects.filter(category=c).exists():
            rp = category(category=c)
            rp.save()
            i = request.POST.get("idea")
            u = ideapeacher.objects.get(user=request.user)
            p = request.FILES.get('pdf')
            d = datetime.now()

            post = idea(peacher=u, Post_idea=i, date_created=d, pdf=p)
            post.save()
            post.category.add(rp)

            return redirect("/home")

        else:

            cp = category.objects.get(category=c)
            i = request.POST.get("idea")
            u = ideapeacher.objects.get(user=request.user)
            p = request.FILES.get('pdf')
            d = timezone.now()

            post = idea(peacher=u, Post_idea=i, date_created=d, pdf=p)
            post.save()
            post.category.add(cp)

    return redirect("/home")

# this view allows to update the edited idea.


@login_required(login_url='login')
@allowed_users(allowed_roles=['ideapeacher'])
def updateidea(request, pk):
    i = idea.objects.get(pk=pk)
    i.Post_idea = request.POST.get('idea')
    i.save()
    return redirect("/home")

# this view allows to delete the idea from the database
@login_required(login_url='login')
@allowed_users(allowed_roles=['ideapeacher'])
def delete_idea(request, pk):
    i = idea.objects.get(pk=pk)
    i.delete()
    return redirect('home')

# this view allows to edit the idea
@login_required(login_url='login')
@allowed_users(allowed_roles=['ideapeacher'])
def edit_idea(request, pk):
    i = idea.objects.get(pk=pk)
    context = {
        'share': i
    }
    return render(request, 'main/edit.html', context)

# this views allows the user to comment on the ideas.


@login_required(login_url='login')
@allowed_users(allowed_roles=['ideapeacher', 'sponsor'])
def comment(request, pk):
    if request.method == "POST":
        f = idea.objects.get(pk=pk)

        i = request.POST.get('comment')
        u = request.user
        d = datetime.now()

        post = Public(comment=i, date_created=d, on_post=f, by=u)
        post.save()

    return redirect("home")

# idea posting template


def post(request):
    return render(request, "main/idea.html")


# view own profile
def profile(request):

    i = idea.objects.all()
    b = Public.objects.all()

    query = ""
    if request.GET:
        query = request.GET['q']
        i = get_data_queryset(str(query))
    return render(request, "main/profile.html", context={'ideas': i, "comments": b})

# first rendering page allows user to choose thier type


def usertype(request):
    return render(request, "main/user.html")
