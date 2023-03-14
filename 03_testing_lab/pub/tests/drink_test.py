import unittest

from src.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.beer = Drink("Beer", 3.00, 20)

    def test_drink_name(self):
        self.assertEqual("Beer", self.beer.name)

    def test_drink_price(self):
        self.assertEqual(3.00, self.beer.price)

