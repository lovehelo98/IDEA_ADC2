from django.urls import path
from .import views
from django.conf.urls import url

from idea.views import PostLikeToogle 


from django.conf.urls.static import static
from django.conf import settings

appname =[
    'idea'
]



urlpatterns = [
    path ('', views.register, name='register'),
    path ("home/", views.homepage, name='homepage'),
    path ('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    

    
    path ('logout/', views.logout_request, name='logout' ),
    path("login/", views.login_request, name="login"),
    url(r'(?P<slug>[\w-]+)/like/$', PostLikeToogle.as_view(), name='like-toggle'),
    path("delete_idea/<int:pk>/", views.delete_idea, name="delete_idea"),
    path("edit_idea/<int:pk>/", views.edit_idea, name="edit_idea"),
    path('list/',views.show_all_data, name='showdata'),
    path('updateapi/<int:pk>/', views.update_data_json,name='updatejson'),
    
] 

(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
