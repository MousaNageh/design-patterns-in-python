"""
definition 1:
Bridge is a structural design pattern that lets you split a large class or a set of closely related classes 
into two separate hierarchies(abstraction and implementation) which can be developed independently of each other.

so the related classes can be connected using abstract classes

definition 2:
The Bridge: design pattern is a structural design pattern that helps in separating the abstraction (the interface) from the implementation,
so that the two can vary independently. 

my definition:
splitting a related classes to abstract and implementation classes, then create a bridge by passing instance as params

This pattern is used to decouple an abstraction from its implementation so that the two can vary independently,promoting flexibility.
The pattern involves an interface which acts as a bridge which makes the functionality of concrete classes independent 
from interface implementer classes. Both types of classes can be altered structurally without affecting each other.

Issue the Bridge Pattern Solves: 
Imagine you're building an application to model shapes. You want to implement two types of shapes (e.g., Circle and Square) 
and two types of colors (e.g., Red and Blue) for each shape. 
Without the Bridge pattern, you might extend each shape class for each color,
resulting in a combinatorial explosion of classes (e.g., RedCircle, BlueCircle, RedSquare, BlueSquare).
"""


class RedCircle:
    def draw(self):
        print("Drawing Circle in Red")


class BlueCircle:
    def draw(self):
        print("Drawing Circle in Blue")


class RedSquare:
    def draw(self):
        print("Drawing Square in Red")


class BlueSquare:
    def draw(self):
        print("Drawing Square in Blue")


"""
In the example above, if you want to introduce a new color or shape,
you have to create a new class for each combination, leading to code duplication and a large number of classes.
"""
