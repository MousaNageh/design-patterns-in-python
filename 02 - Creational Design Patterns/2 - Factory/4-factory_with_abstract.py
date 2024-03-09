from abc import ABC, abstractmethod
from enum import Enum, auto
class HotDrink(ABC):
    
    @abstractmethod
    def consume(self): ...
    

class Tea(HotDrink):
    
    def consume(self):
        print("this is a tea")

class Coffee(HotDrink):
    
    def consume(self):
        print("this is a coffee")


class HotDrinkFactory(ABC):
    
    @abstractmethod
    def prepare(self, amount=1): ...


class TeaFactory(HotDrinkFactory):
    
    def prepare(self, amount=1):
        print(f"preapre {amount!r} cup of tea")
        return [Tea() for _ in range(amount)]
    

class CoffeeFactory(HotDrinkFactory):
    
    def prepare(self, amount=1):
        print(f"preapre {amount!r} cup of coffee")
        return [Coffee() for _ in range(amount)]

def make_drink(type, amount=1):
    if type == 'tea':
        return TeaFactory().prepare(amount=amount)
    elif type == 'coffee':
         return CoffeeFactory().prepare(amount=amount)
# or can make a class 

class DrinkTypes(Enum):
    Coffee = auto()
    Tea = auto()
    

class HotDrinkMachine:
    def __init__(self) -> None:
        self.__factoies = []
        self.__set_drinks()
            
    def __set_drinks(self):
        for drink_type in DrinkTypes:
            factory_instace = eval(drink_type.name + 'Factory')()
            self.__factoies.append(factory_instace)

        

'''
Benefits of This Approach

1 - Encapsulation of Creation Logic: By using factory classes, the logic for creating objects is encapsulated within those factories. 
                                     This makes it easy to change the creation process independently of the client code, enhancing maintainability.

2 - Compliance with Open/Closed Principle: Your system is open for extension but closed for modification. 
                                           You can easily introduce new types of HotDrink and corresponding 
                                           factories without changing the existing code.

3 - Flexibility and Scalability: It's straightforward to add new drink types and their factories, 
                                 making your system highly scalable and flexible to future requirements.

4 - Type Safety and Consistency: The abstract base classes enforce a consistent interface for both drinks and factories, 
                                 ensuring that all concrete implementations adhere to a defined contract. This improves type safety and reliability.
'''