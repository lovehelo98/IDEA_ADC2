from django.urls import path
from .import views
from django.conf.urls import url



appname = [
    'idea'
]

urlpatterns = [
    path ('', views.post, name='post'),
    path("idea/", views.post, name="post"),
# <<<<<<< HEAD
#     path('submitidea/', views.submitidea, name='idea'),
# =======
    
#     path('/submitcomment/', views.submitcomment, name='comment'),
# >>>>>>> 078fe947e42154a8da6611e8c60527b3707cc0a1
    path('updateidea/<int:pk>/', views.updateidea, name='updateidea'),
]

