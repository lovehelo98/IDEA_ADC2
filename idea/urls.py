from django.urls import path
from .import views

urlpatterns = [
    path ('', views.post, name='post'),
    path("idea/", views.post, name="post"),
    path('submitidea/', views.submitidea, name='idea'),
    path('updateidea/<int:pk>/', views.updateidea, name='updateidea'),
]

