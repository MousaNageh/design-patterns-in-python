'''

Observer is a behavioral design pattern:
    that lets you define a subscription mechanism to notify multiple objects about any events that happen to the object they’re observing.

Observable (Subject): will notifies all it's objects

Observer: the object that will receive the event
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