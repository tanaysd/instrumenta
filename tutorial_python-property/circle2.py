
from time import sleep

class Circle2:
    def __init__(self, radius):
        self._radius = radius
        self._diameter = None
        
        
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        self._diameter = None
        self._radius = value
        
    @property
    def diameter(self):
        if self._diameter is None:
            sleep(3)
            self._diameter = self._radius * 2
        return self._diameter
            
