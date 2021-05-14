
from typing import Tuple, Dict, Optional

from .fridge import Fridge, NotEnoughException, ALL_COSTS, ALL_INGREDIENTS
from .pizza import RECIPES


class PizzaMaker:
    def __init__(self, fridge: Fridge):
        self._fridge: Fridge = fridge
        self._gain: float = 0

    @property
    def total_gain(self) -> float:
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
        used = self._fridge.ingredient_used
        for name, amount in used.items():
            if amount == 0:
                continue
            amount += 3  # Buy 3 more
            idx = ALL_INGREDIENTS.index(name)
            cost = ALL_COSTS[idx] * amount
            if cost > self._gain:
                continue
            self._gain -= cost
            self._fridge.add_ingredient(name, amount)
        self._fridge.reset_count()
