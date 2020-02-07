from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from django.conf import settings

# Create your models here.
from django.db import models
from datetime import datetime
from django.utils import timezone


class UserProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    location = models.CharField(max_length=30)
    age = models.IntegerField(blank=True)
    types = (
        ('IDEA PEACHER', 'IDEA PEACHER'),
        ('SPONSOR', 'SPONSOR'),
    )
    Type = models.CharField(max_length=30, null=False,
                            choices=types, default=None)
    image = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return self.user.username

    def create_profile(sender, **kwargs):
        if kwargs['created']:
            user_profile = UserProfile.objects.create(user=kwargs['instance'])

    post_save.connect(create_profile, sender=User)


class category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class idea(models.Model):
    ideaPeacher = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None)
    Post_idea = models.TextField()
    date_created = models.DateTimeField(default=datetime.now())
    category = models.ManyToManyField(category)
    Like = models.ManyToManyField(User, default=True, related_name='post_like')

    def __str__(self):
        return self.Post_idea


class Public(models.Model):
    comment = models.TextField()
    date_created = models.DateTimeField(default=datetime.now())
    on_post = models.ForeignKey(idea, on_delete=models.CASCADE, default=None)
    by = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.comment


class message(models.Model):
    message_text = models.TextField()
    message_time = models.DateTimeField(default=datetime.now())


def get_like_url(self):
    return reverse('post:like-toggle', kwargs={'slug': self.slug})
