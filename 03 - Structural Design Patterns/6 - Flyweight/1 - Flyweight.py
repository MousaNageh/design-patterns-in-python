'''
the flyweight software design pattern refers to an object that minimizes memory usage by sharing some of its data with other similar objects.
so we can make that by saving a shared data extranally
'''
'''
Scenario
Consider a social networking application with millions of users, 
where it's common to have thousands of users with popular names like "John", "Michael", or "Smith". 
Storing these names repeatedly for each user profile would result in unnecessary duplication and increased memory usage.
'''

import string
import random
from abc import ABC, abstractmethod

class NameABC(ABC):
    
    names = []
    @classmethod
    @abstractmethod
    def get_or_set(cls, name): ...
    
    @classmethod
    @abstractmethod
    def get_name(cls, index): ...
    
class Name(NameABC):
    
    @classmethod
    def get_or_set(cls, name: str):
        try:
            return cls.names.index(name)
        except ValueError:
            cls.names.append(name)
            return len(cls.names) - 1 
    
    @classmethod
    def get_name(cls, index: int):
        return cls.names[index]
    
             


class User:
    
    def __init__(self, first_name: str, last_name: str) -> None:
        self._first_name = Name.get_or_set(first_name)
        self._last_name = Name.get_or_set(last_name)
    
    @property
    def first_name(self):
        return Name.get_name(self._first_name)
    
    @first_name.setter
    def first_name(self, first_name: str):
        self._first_name = Name.get_or_set(first_name)
    
    @property
    def last_name(self):
        return Name.get_name(self._last_name)
    
    @last_name.setter
    def last_name(self, last_name: str):
        self._last_name = Name.get_or_set(last_name)
        
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} (first_name: {self.first_name!r}, last_name: {self.last_name!r})>"



def get_name(name_len = 8):
    chars = string.ascii_lowercase 
    return "".join([random.choice(chars) for _ in range(name_len)])

first_names = [get_name() for _ in range(100)]
last_names = [get_name() for _ in range(100)]
users = []

for first_name in first_names:
    for last_name in last_names:
        users.append(User(first_name=first_name, last_name=last_name))
print(Name.names)