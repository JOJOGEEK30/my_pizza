
from sources.fridge import Fridge
from sources.maker import PizzaMaker
from sources.customer import handle_customer_queue


def main():
    fridge = Fridge(default_ingredients=30)
    maker = PizzaMaker(fridge)
    print('Maker: Welcome dear customer, the pizzeria is open !')
    try:
        handle_customer_queue(15, maker)
    except Exception as e:
        print('Maker: Sorry something went wrong. We have to close earlier !')
        print('>>>', e)


if __name__ == '__main__':
    main()
