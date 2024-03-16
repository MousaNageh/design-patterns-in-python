# design patterns in python
- this repo contains explanation of the following :
    
    1. [The SOLID Design Principles](./01%20-%20The%20SOLID%20Design%20Principles) : 
        `The SOLID principles are a set of five design principles intended to make software designs more understandable, flexible, and maintainable. They are a cornerstone of object-oriented design and programming, providing guidelines for writing software that is easy to manage and extend over time. Here's a brief overview of each principle:`

        * [Single Responsibility Principle (SRP)](./01%20-%20The%20SOLID%20Design%20Principles/Single_Responsibility_Principle.py): A class should have only one reason to change, meaning it should have only one job or responsibility. This principle encourages a separation of concerns, leading to more modular and manageable code.

        * [Open/Closed Principle (OCP)](./01%20-%20The%20SOLID%20Design%20Principles/Open_Closed_Principle.py): Software entities (classes, modules, functions, etc.) should be open for extension but closed for modification. This means you should be able to add new functionality to an object or method without changing the existing code that uses it.

        * [Liskov Substitution Principle (LSP)](./01%20-%20The%20SOLID%20Design%20Principles/Liskov_Substitution_Principle.py): Objects in a program should be replaceable with instances of their subtypes without altering the correctness of the program. This principle is fundamental to the design of systems that use inheritance, ensuring that derived classes just extend without replacing the behavior of base classes.

        * [Interface Segregation Principle (ISP)](./01%20-%20The%20SOLID%20Design%20Principles/Interface_Segregation_Principle.py): Clients should not be forced to depend upon interfaces they do not use. This principle encourages splitting large interfaces into smaller, more specific ones so that clients only need to know about the methods that are of interest to them.

        * [Dependency Inversion Principle (DIP)](./01%20-%20The%20SOLID%20Design%20Principles/Dependency_Inversion_Principle.py): High-level modules should not depend on low-level modules. Both should depend on abstractions. Moreover, abstractions should not depend on details; details should depend on abstractions. This principle leads to a decoupling of software modules, making the system more flexible and enabling the independent development and testing of modules.

        ______________________________________________________________
    

    2. [Creational Design Patterns](./02%20-%20Creational%20Design%20Patterns):

        `Creational patterns are focused on how objects are created. They help manage object creation mechanisms, making the system more independent of how its objects are created, composed, and represented. Common creational patterns include:`


        * [builder](./02%20-%20Creational%20Design%20Patterns/1%20-%20builder) : Separates the construction of a complex object from its representation, allowing the same construction process to create different representations. (create step by step)

        * [Factory](./02%20-%20Creational%20Design%20Patterns/2%20-%20Factory) : Defines an interface for creating an object, but lets subclasses decide which class to instantiate.

        * [prototype](./02%20-%20Creational%20Design%20Patterns/3%20-%20prototype) : Creates new objects by copying an existing object, known as the prototype.

        * [singleton](./02%20-%20Creational%20Design%20Patterns/4%20-%20singleton) :  Ensures a class has only one instance and provides a global point of access to it

        ______________________________________________________________
    
    3. [Structural Design Patterns](./03%20-%20Structural%20Design%20Patterns):


        `Structural Design Patterns are a category of design patterns that deal with the composition of classes or objects to form larger structures. They simplify the design by identifying a simple way to realize relationships among entities. The primary focus of structural patterns is on how classes and objects are composed to form larger structures.`

        * [adapter (Wrapper)](./03%20-%20Structural%20Design%20Patterns/1-%20adapter) : Allows incompatible interfaces to work together. It involves a wrapper that translates calls to an object into a different format understood by the object.

        * [bridge](./03%20-%20Structural%20Design%20Patterns/2%20-%20Bridge) : Decouples an abstraction from its implementation so that the two can vary independently.

        * [Composite](./03%20-%20Structural%20Design%20Patterns/3%20-%20Composite) : Composes objects into tree structures to represent part-whole hierarchies, allowing clients to treat individual objects and compositions uniformly.

        * [Decorator](./03%20-%20Structural%20Design%20Patterns/4%20-%20Decorator) : allows behavior to be added to an individual object, either statically or dynamically, without affecting the behavior of other objects from the same class. 

        * [Facade](./03%20-%20Structural%20Design%20Patterns/5%20-%20Facade): provides a simplified interface to a complex subsystem.

        * [Flyweight](./03%20-%20Structural%20Design%20Patterns/6%20-%20Flyweight) : Minimizes memory usage or computational expenses by sharing as much as possible with similar objects; it's about sharing to support large numbers of fine-grained objects efficiently.

        * [Proxy](./03%20-%20Structural%20Design%20Patterns/7%20-%20Proxy) : Provides a surrogate or placeholder for another object to control access to it, useful for lazy loading, controlling access, or logging, for instance.

        ______________________________________________________________

    4. [Behavioral Design Patterns](./04%20-%20Behavioral%20Design%20Patterns)

        `Behavioral design patterns are a group of design patterns that are primarily concerned with algorithms and the assignment of responsibilities between objects. They help manage relationships between objects, making communication between objects easier, more flexible, and more efficient. These patterns focus on how objects interact and distribute responsibility among themselves to perform a task. Here are some of the key behavioral design patterns:`

        
        * [Chain of Responsibility](./04%20-%20Behavioral%20Design%20Patterns/1%20-%20Chain%20of%20Responsibility) : Avoids coupling the sender of a request to its receiver by giving more than one object a chance to handle the request. The request gets passed along a chain of objects until one of them handles it.

        
        * [Command](./04%20-%20Behavioral%20Design%20Patterns/2%20-%20Command) : Encapsulates a request as an object, thereby allowing for the parameterization of clients with queues, requests, and operations. It also allows for the support of undoable operations.


        * [Iterator](./04%20-%20Behavioral%20Design%20Patterns/3%20-%20Iterator) : Provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation. It’s commonly used in Java’s Collection Framework.

        
        * [Mediator](./04%20-%20Behavioral%20Design%20Patterns/4%20-%20Mediator) : Defines an object that encapsulates how a set of objects interact. It promotes loose coupling by keeping objects from referring to each other explicitly and it allows their interaction to be varied independently.

        
        * [Memento](./04%20-%20Behavioral%20Design%20Patterns/5%20-%20Memento) : Provides the ability to restore an object to its previous state (undo via rollback). It is useful for implementing features such as undo mechanisms.

        
        * [Observer](./04%20-%20Behavioral%20Design%20Patterns/6%20-%20Observer) : Defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically. It’s widely used in implementing distributed event handling systems.

        
        * [State](./04%20-%20Behavioral%20Design%20Patterns/7%20-%20State) : Allows an object to alter its behavior when its internal state changes. The object will appear to change its class. This pattern is often used in the context of state machines.

        
        * [Strategy](./04%20-%20Behavioral%20Design%20Patterns/8%20-%20Strategy) : Defines a family of algorithms, encapsulates each one, and makes them interchangeable. Strategy lets the algorithm vary independently from clients that use it. This is useful for algorithms that can be selected at runtime or to provide a variety of behaviors for the same operation.


        * [Template Method](./04%20-%20Behavioral%20Design%20Patterns/9%20-%20Template%20Method) : Defines the skeleton of an algorithm in the superclass but lets subclasses override specific steps of the algorithm without changing its structure. It’s a fundamental technique for code reuse.


        * [Visitor](./04%20-%20Behavioral%20Design%20Patterns/10%20-%20Visitor) : Represents an operation to be performed on the elements of an object structure. Visitor lets you define a new operation without changing the classes of the elements on which it operates. It’s useful when operations need to be added to complex object structures, like document objects or ASTs (Abstract Syntax Trees).



