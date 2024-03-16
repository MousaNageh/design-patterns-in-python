# design patterns in python
- this repo contains explanation of the following :
    
    1. [The SOLID Design Principles](./01%20-%20The%20SOLID%20Design%20Principles)
    
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
