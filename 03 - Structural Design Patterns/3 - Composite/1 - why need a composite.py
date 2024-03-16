"""
Composite: is a structural design pattern that lets you compose objects into tree structures 
and then work with these structures as if they were individual objects. 

This pattern lets clients treat individual objects and compositions of objects uniformly.
It's particularly useful when you want to work with a tree-like structure where
the components can be processed in the same way whether they are complex (composed of other objects) or simple (leaf nodes).
"""

"""
Problem Example
Imagine you're building a file system application where both Files and Folders can be treated similarly.
A Folder can contain multiple Files or other Folders. 
Here, Files can be seen as leaf nodes, whereas Folders are composite objects that can contain leaf nodes or other composites.
"""

"""
Solution with Composite Design Pattern
The Composite Design Pattern solves this problem by defining 
an abstract component class that declares a common interface for both simple (File) and composite (Folder) objects.
Then, both File and Folder classes implement this interface. 
This setup allows you to treat both Files and Folders uniformly by calling their common interface methods.
"""

from abc import ABC, abstractmethod


# Component
class FileSystemComponent(ABC):
    @abstractmethod
    def show(self, indent=0):
        pass


# Leaf
class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def show(self, indent=0):
        print(" " * indent + self.name)


# Composite
class Folder(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component: FileSystemComponent):
        self.children.append(component)

    def remove(self, component: FileSystemComponent):
        self.children.remove(component)

    def show(self, indent=0):
        print(" " * indent + self.name)
        for child in self.children:
            child.show(indent + 2)


# Using the Composite Pattern
if __name__ == "__main__":
    root = Folder("root")
    root.add(File("file1.txt"))
    root.add(File("file2.txt"))

    subFolder = Folder("subfolder")
    subFolder.add(File("file3.txt"))

    root.add(subFolder)
    root.show()
