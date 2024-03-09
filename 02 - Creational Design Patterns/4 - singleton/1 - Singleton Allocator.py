'''

The Singleton Design Pattern is a concept used in software development to ensure that a class has only one instance and provides
a global point of access to that instance.
It's like having a single room in a building where everyone goes to use a particular resource; no matter how many people need it
'''

class Database:
    
    _instance = None 
    _conection = None 
    
    def __init__(self, connection_url: str) -> None:
        if not Database._conection:
            Database._conection = connection_url
    
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance =  super(Database, cls).__new__(cls)
        return cls._instance
    
    @property
    def connection_url(self):
        if self._instance:
            return self._instance._conection
    

d1 = Database(connection_url='connection1')
d2= Database(connection_url='connection2')

print(d1 == d2)
print(d1.connection_url)
print(d2.connection_url)
print(d1._instance._conection)
print(d2._instance._conection)
## the issue here is __init__ is called for every instance