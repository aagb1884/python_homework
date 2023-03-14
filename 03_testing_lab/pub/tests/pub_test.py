import unittest

from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):

    def setUp(self):
        self.pub = Pub("The Crass Badger", 100.00)
        self.drink = Drink("Beer", 3.00, 20)
        self.customer = Customer("Jammo", 10.00, 21, 0)

# can set up basic shop to test and fully stocked one for later

    def test_pub_name(self):
        self.assertEqual("The Crass Badger", self.pub.name)

    def test_pub_till(self):
        self.assertEqual(100.00, self.pub.till)

    # def test_got_drink(self, drink):
    #     self.assertEqual(True, )

    def test_check_age(self):
        self.pub.check_age(self.customer)
        self.assertLessEqual(18, self.customer.age)
        

    def test_sell_drink(self):
        self.pub.sell_drink(self.drink, self.customer)
        self.assertEqual(103.00, self.pub.till)
        self.assertEqual(7.00, self.customer.wallet)
        self.assertGreater(50, self.customer.drunkenness)


        # test check_age for if check_age returns false -
        # i know i've seen this but can't brain it right now