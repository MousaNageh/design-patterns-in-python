"""
The Prototype design pattern is a creational pattern that focuses on copying or cloning objects. 
Instead of creating a new instance of an object from scratch, which can be resource-intensive, 
especially if the object creation involves a lot of steps or complex logic,
you simply clone an existing instance. 
This approach is useful when you want to create an object that is similar to an existing one but may have slight differences.
"""


class Address:

    def __init__(self, street: str, city: str, country: str) -> str:
        self.street = street
        self.city = city
        self.country = country

    def __str__(self) -> str:
        return f"{self.street}, {self.city}, {self.city}"


class Person:

    def __init__(self, name: str, age: int, address: Address) -> str:
        self.name = name
        self.age = age
        self.address = address

    def __str__(self) -> str:
        return f"{self.name}, {self.age} years old, lives at {self.address}"


address1 = Address(street="10 cairo street", city="Cairo", country="Egypt")
john = Person(name="john", age=30, address=address1)
# mousa = Person(name='mousa', age=30 , address=address1)
# mousa levies in the same address or john
# so instead of create new person instance for mousa, what if i can get a copy from john and change the only name
mousa = john
mousa.name = "mousa"
print(mousa.name)  # mousa
print(john.name)  # mousa
# this cope will not work
