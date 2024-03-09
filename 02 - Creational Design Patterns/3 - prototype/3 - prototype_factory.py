'''
let's assume we have only two addresses for offices 
'''
from copy import deepcopy


class Address:
    
    def __init__(self, street: str, city: str, country: str) -> str:
        self.street = street
        self.city = city
        self.country = country 
    
    def __str__(self) -> str:
        return f"{self.street}, {self.city}, {self.city}"
    

class Employee:
    
    def __init__(self, name: str, address: Address) -> None:
        self.name = name 
        self.address = address 
    
    def __str__(self) -> str:
        return f"{self.name}, {self.address}"
        


class EmployeeFactory:
    office_one_employee = Employee(name='', address=Address(street='12 street', city='cairo', country='egpyt'))
    office_two_employee = Employee(name='', address=Address(street='14 street', city='landon', country='UK'))
    custom_address = None
    
    
    @classmethod
    def new_employee_for_office_one(cls, name: str):
        return cls.__new_employee(cls.office_one_employee, name)
    
    @classmethod
    def new_employee_for_office_two(cls, name: str):
        return cls.__new_employee(cls.office_two_employee, name)
    
    @staticmethod
    def __new_employee(prototype: Employee ,name: str):
        employee = deepcopy(prototype)
        employee.name = name 
        return employee
    
    @classmethod
    def new_empoyee_with_custom_address(name: str, address: Address):
        return Employee(name=name, address=address)    

john = EmployeeFactory.new_employee_for_office_one(name='john')