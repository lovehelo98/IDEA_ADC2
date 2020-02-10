
from django.urls import path
from .import views
from ideapeacher.views import *

urlpatterns = [
    path('', views.registersponsor, name='register'),
    path('register/', views.registersponsor, name='register'),
    path('login/', login_request, name="login"), 
    path ("home/", sponsorpage, name='home'),
    path("logout/", logout_request, name='logout'),
    path("comment/<int:pk>/", comment, name="comment"),
    path('profile/', profile, name='profile'),
]


