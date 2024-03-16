"""
To solve this issue (color and shapes),
we use the Bridge pattern by separating the shape and color into separate class hierarchies, allowing them to vary independently.
"""

from abc import ABC, abstractmethod


# abstract color
class Color(ABC):

    @abstractmethod
    def fill_color(ABC): ...


# abstract shape
class Shape(ABC):
    def __init__(self, color: Color):
        # here is the bridge
        self.color: Color = color

    def draw(self):
        pass


# Concrete Implementor 1
class Red(Color):
    def fill_color(self):
        return "Red"


# Concrete Implementor 2
class Blue(Color):
    def fill_color(self):
        return "Blue"


# Refined Abstraction 1
class Circle(Shape):
    def draw(self):
        return f"Drawing Circle in {self.color.fill_color()}"


# Refined Abstraction 2
class Square(Shape):

    def draw(self):
        return f"Drawing Square in {self.color.fill_color()}"


"""
The key advantage of the Bridge design pattern isn't in reducing the total number of classes necessarily,
but in organizing them in a way that reduces the direct dependencies between different dimensions of variability (in this case, shapes and colors). 
This makes your code more modular, easier to understand, and maintain.

Without Bridge Pattern:
Adding N colors and M shapes requires creating N*M classes since each combination of color and shape needs a new class.


With Bridge Pattern:
Adding N colors requires N color classes.
Adding M shapes requires M shape classes.
The total number of classes becomes N + M, not N*M.
"""
