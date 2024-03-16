"""
Problem Example:
Let's consider a scenario where you need to model a hierarchical structure of a company organization.
The organization has departments, which can further contain sub-departments or employees. 
Each employee has a name, position, and salary.
"""

from abc import ABC, abstractmethod
from typing import List


class Hierarichy(ABC):

    @abstractmethod
    def show_hierarichy(self): ...


class Employee(Hierarichy):

    def __init__(self, name: str, dob: str) -> None:
        self.name = name
        self.dob = dob

    def show_hierarichy(self):
        print(self)

    def __str__(self) -> str:
        return f"Employee : name: {self.name}, dob: {self.dob}"


class Department(Hierarichy):

    def __init__(self, name: str) -> None:
        self.name = name
        self.hierarchies: List[Hierarichy] = []

    def add_hierarichy(self, hierarichy: Hierarichy):
        self.hierarchies.append(hierarichy)

    def remove_hierarichy(self, hierarichy: Hierarichy):
        self.hierarchies.remove(hierarichy)

    def show_hierarichy(self):
        print(self.__str__())
        for hierarichy in self.hierarchies:
            hierarichy.show_hierarichy()

    def __str__(self) -> str:
        return f"department : {self.name}"


d1 = Department("d1")
d1.add_hierarichy(hierarichy=Employee(name="emp1", dob="1998-9-9"))
d2 = Department("d2")
d1.add_hierarichy(d2)
d2.add_hierarichy(hierarichy=Employee(name="emp1", dob="1998-9-9"))
d1.show_hierarichy()
