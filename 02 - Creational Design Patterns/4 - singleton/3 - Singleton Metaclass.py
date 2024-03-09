class SingletonMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]



class Database(metaclass=SingletonMeta):
    def __init__(self, connection_url: str) -> None:
        self.connection_url = connection_url
    

p1 = Database(connection_url='connection1')
p2 = Database(connection_url='connection2')

print(p1 == p2)
print(p1.connection_url)
print(p2.connection_url)