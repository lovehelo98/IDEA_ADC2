from django.shortcuts import render, redirect
from .forms import NewForm, UserProfileForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import idea, Public, UserProfile
from django.db.models import Q
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .decorators import unauthenticated_user, admin_only, allowed_users
from datetime import datetime
from django.views.generic import RedirectView


# Create your views here.
def homepage(request):
    i = idea.objects.all()
    b = Public.objects.all()
    query = ""
    if request.GET:
        query = request.GET['q']
        i = get_data_queryset(str(query))

    return render(request, "main/home.html", context={"ideas": i, "comments":b})


def profile(request):
    i = UserProfile.objects.all()
    query = ""
    if request.GET:
        query = request.GET['q']
        i = get_data_queryset(str(query))
    return render(request, "main/profile.html", context={"ideas": i})


def register(request):
    if request.method == "POST":
        form = NewForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()
            return redirect("/login")
    else:
        form = NewForm()
        profile_form = UserProfileForm()
    context = {'form': form, 'profile_form': profile_form}
    return render(request, "main/register.html", context)


def logout_request(request):
    logout(request)
    return redirect("/login")


@unauthenticated_user
def login_request(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)
            return redirect('/home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'main/login.html', context)


def delete_idea(request, pk):
    i = idea.objects.get(pk=pk)
    i.delete()
    return redirect('/home')


def edit_idea(request, pk):
    i = idea.objects.get(pk=pk)
    context = {
        'share': i
    }
    return render(request, 'image/edit.html', context)

# def book_objects_pagination(request,PAGENO,SIZE):
    # skip = SIZE * (PAGENO -1)
    # books = Book.objects.all() [skip:(PAGENO * SIZE)]
    # dict = {
    #         "books":list(Book.values("title","name"))
    # }
    # return JsonResponse(dict)


def get_data_queryset(query):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        u = User.objects.filter(username__icontains=q)
        ideas = idea.objects.filter(
            Q(ideaPeacher__in=u)).distinct()

        for i in ideas:
            queryset.append(i)
    return list(set(queryset))


def show_all_data(request):
    i = idea.objects.all()
    print(type(i))
    dict_type = {"ideas": list(
        i.values("ideaPeacher", "Post_idea", "category", "date_created"))}
    return JsonResponse(dict_type)


@csrf_exempt
def update_data_json(request, pk):
    i = idea.objects.get(id=pk)

    if request.method == "GET":
        return JsonResponse({"Idea": i.Post_idea, "category": i.category})
    else:
        json_body = request.body.decode('utf-8')
        json_data = json.loads(json_body)
        i.Post_idea = json_data['Post_idea']
        i.save()
    return JsonResponse({"message": "Successful!!"})


def comment(request, pk):
    if request.method == "POST":
        f = idea.objects.get(pk=pk) 
        
        i = request.POST.get('comment')
        u = request.user
        d = datetime.now()
        
        
        post = Public(comment=i, date_created=d, on_post=f, by=u)
        post.save()
        
        
        
    return redirect("/home")


class PostLikeToogle(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        obj = get_object_or_404(post, slug=slug)
        url_ = obj.get_absolute_url()
        user = self.request.user
        if user.is_authenticated():
            obj.like.add(user)
        return url_
