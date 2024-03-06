'''
Liskov Substitution Principle (LSP): 
The Liskov substitution principle states that a child class must be substitutable for its parent class.
Liskov substitution principle aims to ensure that the child class can assume the place of its parent class without causing any errors.   
'''
# let's take an example

class Rectangle:
    
    def __init__(self, width: float, height: float) -> None:
        self._width = width
        self._height = height
    
    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height
    
    @property
    def area(self):
        return self._width * self._height
    
    @width.setter
    def width(self, value):
        self._width = value 
    
    @height.setter
    def height(self, value):
        self._height = value 
        
    def __str__(self) -> str:
        return f"width : {self._width}, height : {self._height}"



class Square(Rectangle):
    
    def __init__(self, size: float) -> None:
        super().__init__(width=size, height=size)
    
    
    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value 
    
    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value 
    
        

def use_rectange(rc: Rectangle):
    w = rc.width
    rc.height = 10 
    expected_area = w * 10 
    are = rc.area 
    print("expected_area : ", expected_area) # 50
    print("are : ", are) # 100
    # now we can see that, Square class (which is child class) can not take a place of it's parent class (Rectangle class)
    # so inheritance is not the best idea
    
    
 
    

sq = Square(size=5)

use_rectange(sq)
