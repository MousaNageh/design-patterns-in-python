"""
The Proxy Design Pattern is a structural design pattern that provides a surrogate or placeholder for another object to control access to it.
"""

"""
Types of Proxy Patterns

1 - Virtual Proxy: This type of proxy creates expensive objects on demand. 
    The proxy delays the creation and initialization of the object until it is really needed. 
    This is useful for resource-intensive objects that should not be created until necessary.

2 - Remote Proxy: This proxy provides a local representative for an object that resides in a different address space.
    This is useful in distributed systems, where the object’s actual location in the memory is irrelevant.
    The proxy handles the communication part, allowing clients to work with remote objects in a manner as if they were local.

3 - Protective Proxy: This proxy controls access to a sensitive object by implementing permissions. 
    This is useful when objects should have different access rights. For example, 
    an object might have methods that should be accessible only by a specific group of objects.

4 - Smart Proxy: This proxy adds extra behavior to the object’s operations. 
    This could include adding logging, access control, or caching functionalities. 
    Smart proxies are useful when actions need to be taken before or after the execution of certain operations by the object.

"""
"""
note :
 the proxy must have the same interface as underleying objects
"""
