"""
The Factory Design Pattern is a creational pattern used in object-oriented programming to encapsulate the process of creating objects.
This pattern suggests defining an interface or an abstract class to create objects, 
but allowing subclasses to alter the type of objects that will be created. Essentially, 
it defers instantiation of a class to its subclasses or a dedicated factory class.
"""

# let's show the need of factory
from enum import Enum
from math import sin, cos


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:

    def __init__(self, a, b, system=CoordinateSystem.CARTESIAN) -> None:
        if system == CoordinateSystem.CARTESIAN:
            self.x = a
            self.y = b
        else:
            self.x = a * cos(b)
            self.y = a * sin(b)


# what if i want to add more coordinate systems , the init of the class will be painful
# is the point a and b params is not related to x , y if using CARTESIAN systems
