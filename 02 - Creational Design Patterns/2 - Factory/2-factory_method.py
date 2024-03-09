'''
actory method is any method will create an instance 
this issue here is single responsbility or serpation of concerns, that's why we need factory ant a factory method
'''

from math import sin, cos

class Point:
    
    def __init__(self) -> None:
            self.x = None 
            self.y = None  
    
    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)
    
    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * cos(theta), rho * sin(theta))