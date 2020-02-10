from django.shortcuts import render
from ideapeacher.models import *
from django.http import HttpResponse, JsonResponse
import json 
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# show all data of the idea model using rested client
def show_all_data(request):
    i = idea.objects.all()
    print(type(i))
    dict_type = {"ideas": list(i.values("id","peacher","Post_idea","category","date_created"))}
    return JsonResponse(dict_type)


# update data of the idea model using rested client 
@csrf_exempt
def update_data_json(request, pk):
        i= idea.objects.get(id=pk)
        
        if request.method == "GET":
            return JsonResponse({"Idea":i.Post_idea})
        else:
            json_body = request.body.decode('utf-8')
            json_data = json.loads(json_body)
            i.Post_idea = json_data['Post_idea']
            i.save()
        return JsonResponse({"message":"Successful!!"})


# delete data of the idea model using rested client
@csrf_exempt
def delete_data_json(request, pk):
        try:
            i = idea.objects.get(pk=pk)
            i.delete()
            return JsonResponse({"deleted": True}, safe=False)
        except:
            return JsonResponse({"error": "not a valid primary key"}, safe=False)


# show all the data of the users using rested client 
def users_all_data(request):
    u = ideapeacher.objects.all()
    print(type(u))
    dict_type = {"users": list(u.values("id","user","name"))}
    return JsonResponse(dict_type)


#pagination using rested client.
def idea_objects_pagination(request,PAGENO,SIZE):
    skip = SIZE * (PAGENO -1)
    i = idea.objects.all() [skip:(PAGENO * SIZE)]
    dict = {
            "ideas":list(i.values("peacher","Post_idea","category","date_created"))
    }
    return JsonResponse(dict)
