
class Circle:
    def __init__(self, radius):
        """
        Now you have three methods with the same clean and descriptive attribute-like name. How is that possible?

        The decorator approach for creating properties requires defining a first method using the public name for the underlying managed attribute, which is .radius in this case.
        """
        self._radius = radius
        
    @property
    def radius(self):
        """ The radius property."""
        print("Get radius")
        return self._radius
    
    @radius.setter
    def radius(self, value):
        print("Setting radius")
        self._radius = value
    
    @radius.deleter
    def radius(self):
        print("Deleting radius")
        del self._radius
        
    @property
    def area(self):
        import math
        pi = math.pi
        return float(round(pi * self._radius ** 2), 3)
