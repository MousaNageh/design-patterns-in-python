'''
Interface Segregation Principle (ISP)
The interface segregation principle states clients should not be forced to depend upon methods that they do not use.
clients means the developers that will use these classes that will be inhert from inteface
''so it's better to divide the intefaces'' 
'''

# example 
from abc import ABC, abstractmethod

class Machine(ABC):
    
    @abstractmethod
    def print(self):
        raise NotImplementedError
    
    @abstractmethod
    def scan(self):
        raise NotImplementedError
    
    @abstractmethod
    def fax(self):
        raise NotImplementedError

class MultiFunctionMachine(Machine):
    
    def print(self):
        print("printing ")
    
    def scan(self):
        print("scanning ")
    
    def fax(self):
         print("faxing ")

# the issue here , what if i have a machine can not doing faxing , i will get a problem

class OldMachine(Machine):
    
    def print(self):
        print("printing ")
    
    def scan(self):
        print("scanning ")
    
    def fax(self): ... 
    # i forced to app this method to my class 

# to  solve this $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

class Machine(ABC):
    
    @abstractmethod
    def print(self):
        raise NotImplementedError
    
    @abstractmethod
    def scan(self):
        raise NotImplementedError
    
class Fax:
    
    @abstractmethod
    def fax(self):
        raise NotImplementedError


class MultiFunctionMachine(Machine, Fax):
    
    def print(self):
        print("printing ")
    
    def scan(self):
        print("scanning ")
    
    def fax(self):
         print("faxing ")


class OldMachine(Machine):
    
    def print(self):
        print("printing ")
    
    def scan(self):
        print("scanning ")
    
