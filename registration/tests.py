

# Create your tests here.
from django.test import TestCase
from registration.models import category, message
from datetime import datetime 
# Create your tests here.
class testcategory(TestCase):
    def setUp(self):
        category.objects.create(category='i know all')
        
    def test_ORM(self):
        tut = category.objects.get(category='i know all')
        self.assertEqual(tut.category ,'i know all')

