from django.shortcuts import render
from registration.models import idea

  

def post(request):
        if request.method == 'POST':
            if request.POST.get('Post_category') and request.POST.get('Post_idea'):
                post=idea()
                post.Post_category = request.POST.get('Post_category')
                post.Post_idea= request.POST.get('Post_idea')
                
                post.save()
                
                return render(request, 'image/post.html')  

        else:
                return render(request,'image/post.html')

