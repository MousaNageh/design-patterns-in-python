'''

The Observer Design Pattern is a software design pattern where an object, called the observable,
maintains a list of its dependents, called observers, and notifies them automatically of any state changes, 
usually by calling one of their methods. 
It's a foundational pattern for event-driven programming and is particularly useful in scenarios where an object 
needs to notify other objects about changes in its state.

In the Observer pattern, there are two main components:

Observable (Subject): The entity whose state changes and needs to communicate this change to other objects. 
                It maintains a list of observers and provides mechanisms to add or remove observers from this list. When its state changes,
                it notifies all the registered observers.

Observer: An interface or abstract class defining the update method that will be called by the Observable when its state changes. 
          Concrete implementations of the Observer will process these notifications accordingly.
'''

from typing import  Callable, List

class Observable:
    
    def __init__(self) -> None:
        self._observers: List[Callable] = []
    
    def add_observer(self, observer: Callable):
        self._observers.append(observer)  
    
    def remove_observer(self, observer: Callable):
        self._observers.remove(observer)
    
    def __call__(self, *args, **kwds):
        for observer in self._observers:
            observer(*args, **kwds)        
    

class User:
    
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self._age = age
        self.age_Observable: Observable = Observable()
    
    @property
    def age(self):
        return self.age 
    
    @age.setter
    def age(self, value: int):
        if value == self._age:
            return 
        old_age = self._age
        self._age = value
        self.age_Observable(old_age, self._age)


class AgeTracker:
    
    def __init__(self, user: User) -> None:
        self.user = user
        self.user.age_Observable.add_observer(self.__track_age) 
    
    
    def __track_age(self, old_age, new_age):
        print(f'{self.user.name} has changed his/her name from {old_age} years old to {new_age} years old')

user = User(name='mousa', age=10)
AgeTracker(user)

for i in range(10,30):
    user.age = i