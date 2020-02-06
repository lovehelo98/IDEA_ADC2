from django.shortcuts import render, redirect , get_object_or_404
from main.models import idea , category
from django.utils import timezone 
from datetime import datetime
from django.views.generic.edit import UpdateView
from main.models import idea, Public
from django.views.generic import RedirectView


  

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
       



# class CommentSubmit(RedirectView):
#         def get_redirect_url(self, *args, **kwargs):
#                 slug = self.kwargs.get('slug')
#                 obj = get_object_or_404(post, slug=slug)
#                 url_ = obj.get_absolute_url()
#                 if user.is_authenticated():
#                         i = request.post.get("comment")
#                         u = request.user
#                         d = datetime.now()
#                         f = request.idea

#                         post = Public(public_comment=i, date_created=d, post=f ,by=u,)
#                         post.save()
                        
#                 return url_


class PostLikeToogle(RedirectView):
        def get_redirect_url(self, *args, **kwargs):
                slug = self.kwargs.get('slug')
                obj = get_object_or_404(post, slug=slug)
                url_ = obj.get_absolute_url()
                user = self.request.user
                if user.is_authenticated():
                        obj.like.add(user)
                return url_         





