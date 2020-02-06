from django.urls import path
from .import views
from django.conf.urls import url



appname = [
    'idea'
]

urlpatterns = [
    path ('', views.post, name='post'),
    path("idea/", views.post, name="post"),

    #path('submitidea/', views.submitidea, name='idea'),

    
    #path('/submitcomment/', views.submitcomment, name='comment'),

    path('updateidea/<int:pk>/', views.updateidea, name='updateidea'),
]

