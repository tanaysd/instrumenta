
from functools import cached_property
from time import sleep

class Circle4:
    def __init__(self, radius):
        self._radius = radius
        
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        self._radius = value
        self._diameter = None
        
    @cached_property
    def diameter(self):
        sleep(3)
        return self._radius * 2
