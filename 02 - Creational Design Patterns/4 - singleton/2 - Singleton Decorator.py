'''
Using a decorator is a very elegant and Pythonic way to implement the Singleton pattern. 
A decorator can wrap a class to ensure that only one instance of that class is ever created.
This approach keeps your class definitions clean and separates the singleton logic from the business logic of your class.
'''
from functools import wraps

def singleton(class_):
    instances = {}
    
    @wraps(class_)
    def get_instnace(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return  instances[class_]
    
    return get_instnace


@singleton
class Database:
    def __init__(self, connection_url: str) -> None:
        self.connection_url = connection_url
    

p1 = Database(connection_url='connection1')
p2 = Database(connection_url='connection2')

print(p1 == p2)
print(p1.connection_url)
print(p2.connection_url)