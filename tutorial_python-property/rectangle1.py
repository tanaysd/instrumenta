
class Rectangle1:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    @property
    def area1(self):
        return float(self.width * self.height)
