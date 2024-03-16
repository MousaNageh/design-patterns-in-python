"""
The Monostate (also known as the Borg pattern) is an alternative to the Singleton pattern. 
While the Singleton pattern ensures that a class has only one instance, 
the Monostate pattern allows multiple instances of a class to exist but ensures they all share the same state. 
In other words, each instance of a Monostate class can access and modify the same set of class attributes, 
making their states indistinguishable from one another.
'not recommeded to use it'
"""


class CEO:
    _shared_state = {}

    def __init__(self, name: str, age: int) -> None:
        self.__dict__ = CEO._shared_state
        CEO.name = name
        CEO.age = age

    def __str__(self) -> str:
        return f"name: {self.name}, age: {self.age}"


ceo1 = CEO(name="mousa nageh", age=36)
ceo2 = CEO(name="ahmed mohamed", age=40)

print(ceo1)  # name: ahmed mohamed, age: 40
print(ceo2)  # name: ahmed mohamed, age: 40

# or


class Monostate:

    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls)
        obj.__dict__ = cls._shared_state
        return obj


class CEO(Monostate):

    def __init__(self, name: str, age: int) -> None:
        CEO.name = name
        CEO.age = age

    def __str__(self) -> str:
        return f"name: {self.name}, age: {self.age}"


ceo1 = CEO(name="mousa nageh", age=36)
ceo2 = CEO(name="ahmed mohamed", age=40)

print(ceo1)  # name: ahmed mohamed, age: 40
print(ceo2)  # name: ahmed mohamed, age: 40
