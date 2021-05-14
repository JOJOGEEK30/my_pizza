
from typing import Tuple, Dict, Optional

from .fridge import Fridge, NotEnoughException
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
        except NotEnoughException as e:
            return f'I don\'t have enough "{str(e)}"'
        return None

    def take_an_order(self, name: str) -> Tuple[bool, Optional[str]]:
        if name not in RECIPES:
            return False, 'I don\'t know this pizza'
        ingredients = RECIPES[name]['ingredients']
        price = RECIPES[name]['price']
        self._gain += price  # Gain money
        error = self.__try_to_get_ingredients(ingredients)
        if error is not None:
            return False, error
        return True, None

    def buy_ingredients(self):
        pass
