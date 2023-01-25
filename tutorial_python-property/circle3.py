
from functools import cached_property
from time import sleep

class Circle3:
    def __init__(self, radius):
        self.radius = radius
    
    @cached_property
    def diameter(self):
        sleep(3)
        return self.radius * 2
