
from unittest import TestCase
from random import randint

from sources.maker import PizzaMaker
from sources.fridge import Fridge
from sources.pizza import RECIPES


class TestMaker(TestCase):
    PIZZA_NAMES = tuple(RECIPES.keys())

    def test_not_enough(self):
        maker = PizzaMaker(Fridge())
        pizza_name = self.PIZZA_NAMES[0]
        status, message = maker.take_an_order(pizza_name)
        missing = tuple(RECIPES[pizza_name]['ingredients'].keys())[0]
        self.assertFalse(status)
        self.assertEqual(message, f'I don\'t have enough "{missing}"')

    def test_unknown_pizza(self):
        maker = PizzaMaker(Fridge(15))
        status, error = maker.take_an_order('Invalid pizza name')
        self.assertFalse(status)
        self.assertEqual(error, "I don't know this pizza")


class TestFullMakingGain(TestCase):

    @staticmethod
    def __customer(maker, amount) -> int:
        total_gain = 0
        pizzas = tuple(RECIPES.keys())
        max_idx = len(pizzas) - 1
        for _ in range(amount):
            pizza = pizzas[randint(0, max_idx)]
            status, message = maker.take_an_order(pizza)
            if status:
                total_gain += RECIPES[pizza]['price']
        return total_gain

    def test_few_customer(self):
        maker = PizzaMaker(Fridge(50))
        gain = self.__customer(maker, 10)
        self.assertEqual(gain, maker.total_gain)

    def test_many_customer(self):
        maker = PizzaMaker(Fridge(20))
        gain = self.__customer(maker, 100)
        self.assertEqual(gain, maker.total_gain, msg='The gain is not cancelled')
