'''
1 - Global State: Singleton essentially introduces a global state in your application, 
                  which can lead to hidden dependencies between classes and functions. 
                  This can make the code harder to understand and maintain.


2 - Testing Difficulties: Singletons can make unit testing difficult since they carry state across tests. 
                      This can lead to tests that are dependent on the order in which they are run or require special setup and teardown 
 
                      to reset the state of the singleton, undermining the independence of tests.

3 - Inflexibility: Using the Singleton pattern can make it hard to adapt to changes. 
                   If you later decide that you need multiple instances of the originally singleton class,
                   you'll likely have to make significant changes to your application. Furthermore, 
                   the singleton's global access point is often hard-coded, making it difficult to substitute mock instances for testing.


4 - Concurrency Issues: In multithreaded applications, ensuring that the singleton instance is created only once can lead to complications. 
                         Special care must be taken to synchronize threads during the creation of the singleton object to avoid race conditions.


5 - Inheritance Problems: The Singleton pattern can lead to issues with inheritance. 
                          If a class is designed to be a singleton, extending it to create a subclass can be problematic, 
                          as the subclass inherits the singleton behavior, complicating instance management.
                          

6 - Violation of Single Responsibility Principle: The Singleton pattern often violates the Single Responsibility Principle, 
                                                  as the class has to manage its single instance in addition to its primary responsibilities. 
                                                  This can lead to a class that's harder to understand and maintain.

7  - Potential for Memory Leaks: Since the lifetime of a singleton instance is typically the entire application runtime, 
                                 it can lead to memory leaks, 
                                 especially if the singleton holds onto other resources that should be released or cleaned up.

'''