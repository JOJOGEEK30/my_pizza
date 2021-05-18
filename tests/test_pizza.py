
from unittest import TestCase

from sources.pizza import RECIPES


class TestPizza(TestCase):

    def test_pizza_count(self):
        self.assertTrue(len(RECIPES) >= 10, msg='No pizza added')
