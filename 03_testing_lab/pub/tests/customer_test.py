import unittest

from src.customer import Customer
from src.drink import Drink
from src.pub import Pub
from src.food import Food

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Jammo", 10.00, 21, 0)
        self.drink = Drink("Beer", 3.00, 20)
        self.pub = Pub("The Crass Badger", 100.00)
        self.food = Food("Crisps", 0.50, 5)

    def test_customer_has_name(self):
        self.assertEqual("Jammo", self.customer.name)

    def test_customer_has_money(self):
        self.assertEqual(10.00, self.customer.wallet)

    def test_buy_drink(self):
        self.customer.buy_drink(self.drink)
        self.assertEqual(7.00, self.customer.wallet)
        self.assertEqual(20, self.customer.drunkenness)

    def test_buy_food(self):
        self.customer.buy_food(self.food)
        self.assertEqual(9.50, self.customer.wallet)
        self.assertEqual(25, self.customer.drunkenness)