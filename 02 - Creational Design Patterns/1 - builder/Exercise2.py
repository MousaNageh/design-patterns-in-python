"""
Design a Builder pattern system for constructing different types of cars.
A car's configuration could include the 
1 - engine type (electric, petrol, diesel), 
2 - the color, 
3 - the number of seats, 
4 - and optional features like a sunroof or advanced navigation systems. 
"""

from abc import ABC


class Car:

    def __init__(self):
        self.engine = None
        self.color = None
        self.seats = None
        self.features = []

    def __str__(self) -> str:
        return f"engine :{self.engine}, color: {self.color}, number of seats:{self.seats}  features : {self.features}"

    @staticmethod
    def build():
        return CarBuider()


class CarBuilderABC(ABC):

    def __init__(self, car: Car = None):
        self.car = Car() if not car else car


class CarBuider(CarBuilderABC):

    @property
    def base(self):
        return BaseCarBuilder(car=self.car)

    @property
    def handle_features(self):
        return CarFeatureBuilder(car=self.car)


class BaseCarBuilder(CarBuider):

    def set_engine(self, engine):
        self.car.engine = engine
        return self

    def set_numuber_of_seats(self, seats):
        self.car.seats = seats
        return self

    def set_color(self, color):
        self.car.color = color
        return self


class CarFeatureBuilder(CarBuider):

    def add_feature(self, feature):
        self.car.features.append(feature)
        return self

    def remove_feature(self, index):
        del self.car.features[index]
        return self


build_car = (
    Car.build().base.set_color("red").set_engine("electric").set_numuber_of_seats(4)
)
build_car.handle_features.add_feature("feature 1")

print(build_car.car)
