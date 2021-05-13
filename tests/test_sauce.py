
from unittest import TestCase

from sources.maker import PizzaMaker
from sources.pizza import RECIPES
from sources.fridge import Fridge


class TestSauce(TestCase):
    def test_valid(self):
        fridge = Fridge(default_ingredients=100)
        maker = PizzaMaker(fridge)
        pizza_name = tuple(RECIPES.keys())[-1]
        old = fridge.total_sauce_unit
        status, message = maker.take_an_order(pizza_name)
        self.assertEqual(old, fridge.total_sauce_unit + 1)
        self.assertTrue(status)
        self.assertIsNone(message)
        fridge.empty_sauce_jars()
        self.assertEqual(fridge.total_sauce_unit, 0)
        status, message = maker.take_an_order(pizza_name)
        self.assertTrue(status)
        self.assertEqual(message, 'Sorry for the wait, I had to refill the sauce jar.')
