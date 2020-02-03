from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models
from datetime import datetime
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30)
    age = models.IntegerField()
    types = (
        ('IDEA PEACHER','IDEA PEACHER'),
        ('SPONSOR','SPONSOR'),
    )
    Type = models.CharField(max_length=30, null=False, choices=types, default=None)

    def __str__(self):
        return self.user.username


class category(models.Model):
    category   = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class idea(models.Model):
    ideaPeacher= models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    Post_idea = models.TextField()
    date_created = models.DateTimeField(default=datetime.now()) 
    category = models.ManyToManyField(category)

    def __str__(self):
        return self.Post_idea


class Public(models.Model):
    public_comment = models.TextField()
    date_created = models.DateTimeField(default=datetime.now()) 
    post = models.ForeignKey(idea, on_delete=models.CASCADE, default=None)
    by = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
   
    
    def __str__(self):
        return self.public_comment


class message(models.Model):
    message_text = models.TextField()
    message_time = models.DateTimeField(default=datetime.now())
    