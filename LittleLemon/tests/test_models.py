from restaurant.models import MenuItem
from django.test import TestCase
from decimal import Decimal

#TestCase class
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=80.00, inventory=10)
        self.assertEqual(str(item), "IceCream : 80.00")
        #self.assertEqual(item.title, "IceCream")
        #self.assertEqual(item.price, Decimal(80.00))