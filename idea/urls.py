from django.urls import path
from .import views
from django.conf.urls import url

from idea.views import CommentSubmit

appname = [
    'idea'
]

urlpatterns = [
    path ('', views.post, name='post'),
    path("idea/", views.post, name="post"),
    path('submitidea/', views.submitidea, name='idea'),
    url(r'(?P<slug>[\w-]+)/comment/$', CommentSubmit.as_view(), name='comment'),
    path('updateidea/<int:pk>/', views.updateidea, name='updateidea'),
]

