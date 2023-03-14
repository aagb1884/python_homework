import unittest

class TestFood(unittest.TestCase):

    def setUp(self):
        self.food = Food("Crisps", 0.50, 5)