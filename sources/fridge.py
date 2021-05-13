
from typing import Dict

ALL_INGREDIENTS = ('ham', 'mozzarella', 'parmesan', 'gorgonzola', 'onion', 'olive',
                   'pepper', 'garlic', 'basil', 'mushroom', 'cheddar', 'oregano')


class UnknownIngredientException(Exception):
    def __init__(self, ingredient: str):
        self._ingredient = ingredient

    def __str__(self):
        return f'Ingredient "{self._ingredient}" is not known'


class NotEnoughException(Exception):
    pass


class Fridge:
    def __init__(self, default: int = 0):
        self._ingredients: Dict[str, int] = dict.fromkeys(ALL_INGREDIENTS, default)

    @property
    def is_empty(self) -> bool:
        return all(v == 0 for v in self._ingredients.values())

    def add_ingredient(self, name: str, amount: int) -> None:
        if name not in self._ingredients:
            raise UnknownIngredientException(name)
        if amount <= 0:
            raise ValueError('Amount should be positive')
        self._ingredients[name] += amount

    def add_multiple_ingredients(self, ingredients: Dict[str, int]):
        for name, amount in ingredients.items():
            self.add_ingredient(name, amount)

    def use_ingredient(self, name: str, amount: int):
        if name not in self._ingredients:
            raise UnknownIngredientException(name)
        if self._ingredients[name] < amount:
            raise NotEnoughException(name)
        if amount <= 0:
            raise ValueError('Amount should be positive')
        self._ingredients[name] -= amount

    def use_multiple_ingredients(self, ingredients: Dict[str, int]) -> None:
        taken: Dict[str, int] = dict()
        for name, amount in ingredients.items():
            try:
                self.use_ingredient(name, amount)
            except NotEnoughException as e:
                self.add_multiple_ingredients(taken)  # Replace taken ingredients
                raise e
            else:
                taken[name] = amount
        return
