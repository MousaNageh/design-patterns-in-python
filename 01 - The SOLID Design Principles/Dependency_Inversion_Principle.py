'''
Dependency Inversion Principle (DIP)
High-level modules should not depend on low-level modules. Both should depend on abstractions.
Abstractions should not depend on details. Details should depend on abstractions.
'''
from enum import Enum
from abc import ABC, abstractmethod
class Relation(Enum):
    PARENT =1 
    CHILD = 2 
    SPLINING = 3 


class Person:
    def __init__(self, name) -> None:
        self.name = name  
      
    def __eq__(self, other) -> bool:
        return self.name == other.name 
    
    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return self.name


class Relationship:
    
    def __init__(self) -> None:
        self.relationships = []
    
    def add_parent_and_child(self, parent:Person , child: Person):
        self.relationships.append(
            (parent, Relation.CHILD, child)
        )
        self.relationships.append(
            (child, Relation.PARENT, parent)
        )


class Research:
    def __init__(self, relatiobship: Relationship, person: Person) -> None:
        for relation in relatiobship.relationships:
            if relation[0] == person and relation[1] == Relation.CHILD:
                print(f"{person!r} has a child called {relation[2]!r}")
        # the issue here is Research (high level module) depends on the type of relationship if it list or table, 
        # it should depends on abstruction of Relationship not on the implementation
        
        
# to solve this $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


class RelationshipAbstruct(ABC):
    
    @abstractmethod
    def find_all_childs_of(self, person: Person): ...


class Relationship(RelationshipAbstruct): # low level module
    
    def __init__(self) -> None:
        self.relationships = []
    
    def add_parent_and_child(self, parent:Person , child: Person):
        self.relationships.append(
            (parent, Relation.CHILD, child)
        )
        self.relationships.append(
            (child, Relation.PARENT, parent)
        )
    
    def find_all_childs_of(self, person: Person):
        for relation in self.relationships:
             if relation[0] == person and relation[1] == Relation.CHILD:
                 yield relation[2]



class Research: # high level module
    def __init__(self, relatiobship: RelationshipAbstruct, person: Person) -> None:
            for child in relatiobship.find_all_childs_of(person):
                print(f"{person!r} has a child called {child!r}")


parent = Person('John')
child1 = Person('chris')
child2 = Person('matt')
child3 = Person('mary')
relationship  = Relationship()
relationship.add_parent_and_child(parent=parent, child=child1)
relationship.add_parent_and_child(parent=parent, child=child2)
relationship.add_parent_and_child(parent=parent, child=child3)

Research(relatiobship=relationship, person=parent)

