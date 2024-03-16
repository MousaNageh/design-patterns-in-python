"""
Create a Builder pattern implementation for a pizza ordering system. 
The goal is to allow customers to build their custom pizza by choosing different ingredients like the crust type, sauce, cheese, and toppings.
"""

from abc import ABC, abstractmethod


class Pizza:

    def __init__(self):
        self.name = ""
        self.type = None
        self.price = None

    @staticmethod
    def build():
        return PizzaBuild()

    def __str__(self) -> str:
        return f"name : {self.name}, type : {self.type}, price: {self.price}"


class PizzaBuildABC(ABC):

    def __init__(self) -> None:
        self.pizza = Pizza()

    @abstractmethod
    def set_name(self, value): ...

    @abstractmethod
    def set_type(self, value): ...

    @abstractmethod
    def set_price(self, value): ...

    def build(self):
        return self.pizza


class PizzaBuild(PizzaBuildABC):

    def set_name(self, value):
        self.pizza.name = value
        return self

    def set_price(self, value):
        self.pizza.price = value
        return self

    def __str__(self) -> str:
        return str(self.pizza)


pizze = Pizza.build().set_name("pizza 1").set_price(12).set_type("sauce").build()
print(pizze)
