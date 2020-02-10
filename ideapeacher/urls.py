from django.urls import path
from .import views  
from sponsor.views import *
from restapi.views import *

urlpatterns = [
    path('', views.usertype, name='type'),
    path('peacher/', views.registerpeacher, name='register'),
    path('sponsor/', registersponsor, name='register'),
    path('login/', views.login_request, name="login"), 
    path ("home/", views.ideapeacherpage, name='home'),
    path("sponsorpage/", views.sponsorpage, name='sponsor'),
    path("logout/", views.logout_request, name='logout'),
    path("idea/", views.post, name='post'),
    path("submitidea/", views.submitidea, name='submitidea'),
    path('delete_idea/<int:pk>/', views.delete_idea, name="delete_idea"),
    path('edit_idea/<int:pk>/', views.edit_idea, name="edit_idea"),
    path("comment/<int:pk>/", views.comment, name="comment"),
    path('profile/', views.profile, name='profile'),
    path('updateidea/<int:pk>/', views.updateidea, name='updateidea'),
    path('list/',show_all_data, name='showdata'),
    path('updateapi/<int:pk>/', update_data_json,name='updatejson'),
    path('deleteapi/<int:pk>/', delete_data_json, name='deleteapi' ),
    path('usersapi/', users_all_data, name = 'userapi'),
    path("pagination/<int:PAGENO>/<int:SIZE>/", idea_objects_pagination, name="pagination"),
]