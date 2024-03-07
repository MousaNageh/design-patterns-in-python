'''

When dealing with complex building processes that might require more than one build strategy, 
the Builder pattern still applies, 
but you might need to introduce additional layers of abstraction or utilize different types of builders to accommodate the complexity.
Let's consider a new example to explain this scenario: building a customizable House.

Scenario
Suppose you're building a software to model house construction. 
A house can have various features: number of floors, type of roof, presence of a garden, etc. 
You might want different types of houses, such as a simple one-story house, 
a two-story house with a garden, or a luxury villa.
'''
from abc import ABC, abstractclassmethod

# Product
class House:
    def __init__(self):
        self.floors = None
        self.roof = None
        self.garden = False

#build 
class HouseBuilder(ABC):
    
    @abstractclassmethod
    def set_floors(self, number): ...
    
    @abstractclassmethod
    def set_roof(self, roof_type):...
    
    @abstractclassmethod
    def set_garden(self, has_garden):...
    
    @abstractclassmethod
    def get_house(self): ...


#Concrete Builders
class SimpleHouseBuilder(HouseBuilder):
    def __init__(self):
        self.house = House()
    
    # Implementations of building steps...

class LuxuryVillaBuilder(HouseBuilder):
    def __init__(self):
        self.house = House()
    
    # Implementations of building steps...

#Director
class HouseDirector:
    def __init__(self, builder):
        self._builder = builder

    def construct_simple_house(self):
        self._builder.set_floors(1)
        self._builder.set_roof('simple')

    def construct_luxury_villa(self):
        self._builder.set_floors(2)
        self._builder.set_roof('tile')
        self._builder.set_garden(True)
