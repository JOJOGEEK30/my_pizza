
from typing import Tuple, Dict, Optional

from .fridge import Fridge, NotEnoughIngredientException, NotEnoughSauceException
from .pizza import RECIPES


class PizzaMaker:
    def __init__(self, fridge: Fridge):
        self._fridge: Fridge = fridge
        self._gain: int = 0

    @property
    def total_gain(self) -> int:
        return self._gain

    def __try_to_get_ingredients(self, ingredients: Dict[str, int]) -> Optional[str]:
        try:
            self._fridge.use_multiple_ingredients(ingredients)
        except NotEnoughIngredientException as e:
            return f'I don\'t have enough "{str(e)}"'
        return None

    def __apply_sauce(self, pizza: Dict) -> Optional[str]:
        try:
            sauce = pizza['sauce']
        except KeyError:
            return
        try:
            self._fridge.use_sauce(sauce)
        except NotEnoughSauceException:
            self._fridge.refill_sauce()
            self.__apply_sauce(pizza)
            return 'Sorry for the wait, I had to refill the sauce jar.'
        return

    def take_an_order(self, name: str) -> Tuple[bool, Optional[str]]:
        if name not in RECIPES:
            return False, 'I don\'t know this pizza'
        ingredients = RECIPES[name]['ingredients']
        price = RECIPES[name]['price']
        self._gain += price  # Gain money
        error = self.__try_to_get_ingredients(ingredients)
        if error is not None:
            return False, error
        message = self.__apply_sauce(RECIPES[name])
        return True, message
