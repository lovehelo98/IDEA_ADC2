from django.test import TestCase
from .models import *
from django.contrib.auth.models import User
from datetime import datetime

# Create your tests here.


class firsttest(TestCase):
    def setUp(self):
        i = category.objects.create(category="Health")

    def test_data(self):
        c = category.objects.get(category="Health")
        self.assertEqual(c.category, "Health")


class secondtest(TestCase):
    def setUp(self):
        user = User.objects.create_user('foo', password='bar')
        i = ideapeacher.objects.create(user=user, name="love")

    def test_data(self):
        i = ideapeacher.objects.get(name="love")
        self.assertEqual(i.name, "love")


class thirdtest(TestCase):
    def setUp(self):
        user = User.objects.create_user('foo', password='bar')
        i = ideapeacher.objects.create(user=user, name="love")
        c = idea.objects.create(
            peacher=i, Post_idea="hey", date_created=timezone.now())

    def test_data(self):
        g = idea.objects.get(Post_idea="hey")
        self.assertEqual(g.Post_idea, "hey")


class Fourthtest(TestCase):
    def setUp(self):
        user = User.objects.create_user('foo', password='bar')
        i = ideapeacher.objects.create(user=user, name="love")
        c = idea.objects.create(
            peacher=i, Post_idea="hey", date_created=timezone.now())
        p = Public.objects.create(
            comment="nice", date_created=timezone.now(), on_post=c, by=user)

    def test_data(self):
        g = Public.objects.get(comment="nice")
        self.assertEqual(g.comment, "nice")


class fifthtest(TestCase):
    def setUp(self):
        t = message.objects.create(
            message_text="hi", message_time=timezone.now())

    def test_data(self):
        r = message.objects.get(message_text="hi")
        self.assertEqual(r.message_text, "hi")
