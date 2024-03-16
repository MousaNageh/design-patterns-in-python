# design patterns in python
- this repo contains explanation of the following :
    
    1. [The SOLID Design Principles](./01%20-%20The%20SOLID%20Design%20Principles) : 
        `The SOLID principles are a set of five design principles intended to make software designs more understandable, flexible, and maintainable. They are a cornerstone of object-oriented design and programming, providing guidelines for writing software that is easy to manage and extend over time. Here's a brief overview of each principle:`

        * `Single Responsibility Principle (SRP):` A class should have only one reason to change, meaning it should have only one job or responsibility. This principle encourages a separation of concerns, leading to more modular and manageable code.

        * `Open/Closed Principle (OCP):` Software entities (classes, modules, functions, etc.) should be open for extension but closed for modification. This means you should be able to add new functionality to an object or method without changing the existing code that uses it.

        * `Liskov Substitution Principle (LSP):` Objects in a program should be replaceable with instances of their subtypes without altering the correctness of the program. This principle is fundamental to the design of systems that use inheritance, ensuring that derived classes just extend without replacing the behavior of base classes.

        * `Interface Segregation Principle (ISP):` Clients should not be forced to depend upon interfaces they do not use. This principle encourages splitting large interfaces into smaller, more specific ones so that clients only need to know about the methods that are of interest to them.

        * `Dependency Inversion Principle (DIP):` High-level modules should not depend on low-level modules. Both should depend on abstractions. Moreover, abstractions should not depend on details; details should depend on abstractions. This principle leads to a decoupling of software modules, making the system more flexible and enabling the independent development and testing of modules.

    

    2. [Creational Design Patterns](./02%20-%20Creational%20Design%20Patterns):

        `Creational patterns are focused on how objects are created. They help manage object creation mechanisms, making the system more independent of how its objects are created, composed, and represented. Common creational patterns include:`


        * [builder](./02%20-%20Creational%20Design%20Patterns/1%20-%20builder) : Separates the construction of a complex object from its representation, allowing the same construction process to create different representations. (create step by step)

        * [Factory](./02%20-%20Creational%20Design%20Patterns/2%20-%20Factory) : Defines an interface for creating an object, but lets subclasses decide which class to instantiate.

        * [prototype](./02%20-%20Creational%20Design%20Patterns/3%20-%20prototype) : Creates new objects by copying an existing object, known as the prototype.

        * [singleton](./02%20-%20Creational%20Design%20Patterns/4%20-%20singleton) :  Ensures a class has only one instance and provides a global point of access to it
    
    
    3. [Structural Design Patterns](./03%20-%20Structural%20Design%20Patterns):


        `Structural Design Patterns are a category of design patterns that deal with the composition of classes or objects to form larger structures. They simplify the design by identifying a simple way to realize relationships among entities. The primary focus of structural patterns is on how classes and objects are composed to form larger structures.`

        * [adapter (Wrapper)](./03%20-%20Structural%20Design%20Patterns/1-%20adapter) : Allows incompatible interfaces to work together. It involves a wrapper that translates calls to an object into a different format understood by the object.

        * [bridge](./03%20-%20Structural%20Design%20Patterns/2%20-%20Bridge) : Decouples an abstraction from its implementation so that the two can vary independently.

        * [Composite](./03%20-%20Structural%20Design%20Patterns/3%20-%20Composite) : Composes objects into tree structures to represent part-whole hierarchies, allowing clients to treat individual objects and compositions uniformly.

        * [Decorator](./03%20-%20Structural%20Design%20Patterns/4%20-%20Decorator) : allows behavior to be added to an individual object, either statically or dynamically, without affecting the behavior of other objects from the same class. 

        * [Facade](./03%20-%20Structural%20Design%20Patterns/5%20-%20Facade): provides a simplified interface to a complex subsystem.

        * [Flyweight](./03%20-%20Structural%20Design%20Patterns/6%20-%20Flyweight) : Minimizes memory usage or computational expenses by sharing as much as possible with similar objects; it's about sharing to support large numbers of fine-grained objects efficiently.

        * [Proxy](./03%20-%20Structural%20Design%20Patterns/7%20-%20Proxy) : Provides a surrogate or placeholder for another object to control access to it, useful for lazy loading, controlling access, or logging, for instance.
