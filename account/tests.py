from django.test import TestCase
from .models import TestCase
# Create your tests here.

class RestaurantModelTest(TestCase):
    def test_restaurant_creation(self):
        restaurant = Restaurant.object.create(name="Tasty Bites")
        self.assertEqual(restaurant.name,"Tasty Bites")
        