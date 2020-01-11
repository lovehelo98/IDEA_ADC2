from django.urls import path
from .import views

urlpatterns = [
    path ('', views.register, name='register'),
    path ("home/", views.homepage, name='homepage'),
    path ('register/', views.register, name='register'),
    
   path ('logout/', views.logout_request, name='logout' ),
   path("login/", views.login_request, name="login"),
  
]
