
import math

class Point6:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    @property
    def distance(self):
        return round(math.dist((0, 0), (self.x, self.y)))
    
    @property
    def angle(self):
        return round(math.degrees(math.atan(self.y / self.x)), 1)
    
    @property
    def as_cartesian(self):
        return self.x, self.y
    
    @property
    def as_polar(self):
        return self.distance, self.angle

        
