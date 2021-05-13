
from typing import Dict

ALL_INGREDIENTS = ('ham', 'mozzarella', 'parmesan', 'gorgonzola', 'onion', 'olive',
                   'pepper', 'garlic', 'basil', 'mushroom', 'cheddar', 'oregano')

ALL_SAUCES = ('tomato', 'cream')


class UnknownIngredientException(Exception):
    def __init__(self, ingredient: str):
        self._ingredient = ingredient

    def __str__(self):
        return f'Ingredient "{self._ingredient}" is not known'


class NotEnoughException(Exception):
    pass


class NotEnoughSauceException(NotEnoughException):
    pass


class NotEnoughIngredientException(NotEnoughException):
    pass


class Fridge:
    def __init__(self, default_ingredients: int = 0, default_sauce: int = 4):
        if default_ingredients < 0:
            default_ingredients = 0
        if default_sauce < 0:
            default_sauce = 0
        self._ingredients: Dict[str, int] = dict.fromkeys(ALL_INGREDIENTS, default_ingredients)
        self._sauces: Dict[str, int] = dict.fromkeys(ALL_SAUCES, default_sauce)

    @property
    def is_empty(self) -> bool:
        return all(v == 0 for v in self._ingredients.values())

    @property
    def total_sauce_unit(self) -> int:
        return sum(self._sauces.values())

    def empty_sauce_jars(self):
        for name in self._sauces:
            self._sauces[name] = 0

    def use_sauce(self, name: str):
        if name not in self._sauces:
            raise UnknownIngredientException('sauce ' + name)
        if self._sauces[name] < 1:
            raise NotEnoughSauceException()
        self._sauces[name] -= 1

    def refill_sauce(self, amount: int = 4):
        for key in self._sauces.keys():
            self._sauces[key] = amount

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
            raise NotEnoughIngredientException(name)
        if amount <= 0:
            raise ValueError('Amount should be positive')
        self._ingredients[name] -= amount

    def use_multiple_ingredients(self, ingredients: Dict[str, int]) -> None:
        taken: Dict[str, int] = dict()
        for name, amount in ingredients.items():
            try:
                self.use_ingredient(name, amount)
            except NotEnoughIngredientException as e:
                self.add_multiple_ingredients(taken)  # Replace taken ingredients
                raise e
            else:
                taken[name] = amount
        return
