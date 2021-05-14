
from sources.fridge import Fridge
from sources.maker import PizzaMaker
from sources.customer import handle_days


def main():
    fridge = Fridge(15)
    maker = PizzaMaker(fridge)
    print('Maker: Welcome dear customer, the pizzeria is open !')
    try:
        handle_days(3, maker, 4)
    except Exception as e:
        print('Maker: Sorry something went wrong. We have to close earlier !')
        print('>>>', e)


if __name__ == '__main__':
    main()
