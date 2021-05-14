
from random import randint

from .pizza import RECIPES
from .maker import PizzaMaker


def handle_customer_queue(amount: int, maker: PizzaMaker):
    pizzas = tuple(RECIPES.keys())
    max_idx = len(pizzas) - 1
    for customer_id in range(amount):
        customer_id += 1
        print('Maker: Welcome to you Customer {:02d} !'.format(customer_id))
        pizza = pizzas[randint(0, max_idx)]
        print('Customer {:02d}: I want a "{}" please'.format(customer_id, pizza))
        status, message = maker.take_an_order(pizza)
        if not status:
            print('Maker: Sorry but', message)
        else:
            print(f'Maker: Here is your "{pizza}" !')
            print('Customer {:02d}: Thank you !'.format(customer_id))


def handle_days(amount: int, maker: PizzaMaker, customer_amount: int = 10):
    for day_id in range(amount):
        print('===  Day {:02d}        ==='.format(day_id + 1))
        handle_customer_queue(customer_amount, maker)
        maker.buy_ingredients()
        print('>>> Gain:', maker.total_gain)
        print('=== End of the day ===')
    pass
