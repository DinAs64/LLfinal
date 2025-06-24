from django.test import TestCase
from restaurant.models import MenuItem
import restaurant.urls
from restaurant.serializers import MenuSerializer
from rest_framework import status
from django.urls import reverse

class MenuViewTest(TestCase):
    def setUp(self):
        MenuItem.objects.create(title="IceCream", price="80.00", inventory=5)
        MenuItem.objects.create(title="Pizza", price="150.00", inventory=7)
    
    def test_getall(self):
        items = MenuItem.objects.all()

        url = reverse('menu')
        response = self.client.get(url)
        expected_data = MenuSerializer(items, many=True).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)
