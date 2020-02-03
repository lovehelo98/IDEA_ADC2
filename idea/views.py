from django.shortcuts import render, redirect 
from main.models import idea , category
from django.utils import timezone 
from datetime import datetime
from django.views.generic.edit import UpdateView
from main.models import idea, Public


  

def post(request):
        return render (request, "image/idea.html")

def submitidea(request):
        if request.method=="POST":
                c = request.POST.get("dropdown")
        if not   category.objects.filter(category=c).exists():
                rp = category(category=c)
                rp.save()
                i = request.POST.get("idea")
                u = request.user
                d = datetime.now()

                post = idea(ideaPeacher=u,Post_idea=i,date_created=d)
                post.save()
                post.category.add(rp)
        
                return redirect ("/home")
        
        else : 

                cp = category.objects.get(category=c)
                i = request.POST.get("idea")
                u = request.user
                d = timezone.now()

                post = idea(ideaPeacher=u,Post_idea=i,date_created=d)
                post.save()
                post.category.add(cp)

                return redirect ("/home")

def updateidea(request, pk):
    i = idea.objects.get(pk=pk)
    i.Post_idea = request.POST.get('idea')
    i.save()
    return redirect("/home")
       



