"""
The Builder design pattern is a creational pattern used to construct complex objects step by step. 
It is especially useful when an object needs to be created with many optional components or configurations. 
The main idea is to separate the construction of a complex object from its representation,
allowing the same construction process to create different representations.

Key Components

1 - Product: The complex object that is being built.

3 - Builder interface: Provides an interface for adding parts to the object being built. (optional)

4 - Concrete Builder: Implements the Builder interface and provides specific implementations for the steps 
    required to build a particular representation of the product. It keeps track of the representation it 
    creates and provides a method to retrieve the finished product.

3 - Director: Constructs an object using the Builder interface (optional).

"""

"""
Example: Building a Computer

Let's consider an example where we want to build a customized Computer.
A Computer can have several components such as the CPU, GPU, memory, and storage. 
Not all computers will have the same components; some may have a high-end GPU, while others might not include one at all.

"""
from abc import ABC, abstractclassmethod


# Product
class Computer:
    def __init__(self):
        self.cpu = None
        self.gpu = None
        self.memory = None
        self.storage = None

    def __str__(self):
        return f"Computer(CPU: {self.cpu}, GPU: {self.gpu}, Memory: {self.memory}, Storage: {self.storage})"

    @staticmethod
    def build():
        return MyComputerBuilder(computer=Computer())


# Builder Interface
class ComputerBuilder(ABC):

    @abstractclassmethod
    def set_cpu(self, cpu): ...

    @abstractclassmethod
    def set_gpu(self, gpu): ...

    @abstractclassmethod
    def set_memory(self, memory): ...

    @abstractclassmethod
    def set_storage(self, storage): ...

    @abstractclassmethod
    def get_computer(self): ...


# Concrete Builder
class MyComputerBuilder(ComputerBuilder):
    def __init__(self, computer: Computer = None):
        self.computer = Computer() if not computer else computer

    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def set_gpu(self, gpu):
        self.computer.gpu = gpu
        return self

    def set_memory(self, memory):
        self.computer.memory = memory
        return self

    def set_storage(self, storage):
        self.computer.storage = storage
        return self

    def get_computer(self):
        return self.computer


# Director
class ComputerDirector:
    def __init__(self, builder: ComputerBuilder):
        self._builder = builder

    def build_minimal_viable_computer(self):
        self._builder.set_cpu("i5")
        self._builder.set_memory("8GB")

    def build_full_featured_computer(self):
        self._builder.set_cpu("i9")
        self._builder.set_gpu("RTX 3080")
        self._builder.set_memory("32GB")
        self._builder.set_storage("1TB SSD")


builder = Computer.build()
director = ComputerDirector(builder)

# Build a minimal computer
director.build_minimal_viable_computer()
minimal_computer = builder.get_computer()
print(minimal_computer)

# Build a fully-featured computer
director.build_full_featured_computer()
full_computer = builder.get_computer()
print(full_computer)
