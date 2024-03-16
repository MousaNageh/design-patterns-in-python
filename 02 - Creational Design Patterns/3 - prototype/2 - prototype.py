from copy import deepcopy


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
mousa = deepcopy(
    john
)  # this instance created from anther instance not from original class

mousa.name = "mousa"
mousa.address.street = "11 cairo street"
print(mousa)
print(john)
