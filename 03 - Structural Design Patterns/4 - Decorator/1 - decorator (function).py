'''
The Decorator design pattern is a structural pattern used to extend the functionality of objects dynamically without changing their implementation.
It achieves this by creating a set of decorator classes that are used to wrap concrete components. 
This pattern is particularly useful when you want to add responsibilities to individual objects without affecting other objects or the structure of object classes.
'''
from functools import wraps
import time

def seep_time(time_ =1):
    
    def time_op(func):
        @wraps(func)
        def decorator(*args, **kwargs):
            print(f'sleeping for {time_} sec')
            time.sleep(1)
            return func(*args, **kwargs)
        return decorator
    return time_op

@seep_time()
def some_ops():
    print("working on it ....")


for _ in range(5):
    some_ops()