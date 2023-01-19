
class Circle:
    def __init__(self, radius):
        """
        The following example shows how to create a Circle class with a handy property to manage its radius
        
        In this code snippet, you create Circle. The class initializer, .__init__(), takes radius as an argument and stores it in a non-public attribute called ._radius. Then you define three non-public methods:

        ._get_radius() returns the current value of ._radius
        ._set_radius() takes value as an argument and assigns it to ._radius
        ._del_radius() deletes the instance attribute ._radius
        Once you have these three methods in place, you create a class attribute called .radius to store the property object. 
        To initialize the property, you pass the three methods as arguments to property(). You also pass a suitable docstring for your property.
        """
        self._radius = radius
        
    def _get_radius(self):
        print("Get radius")
        return self._radius
    
    def _set_radius(self, value):
        print("Setting radius")
        self._radius = value
        
    def _del_radius(self):
        print("Deleting radius")
        del self._radius
        
    radius = property(
        fget=_get_radius,
        fset=_set_radius,
        fdel=_del_radius,
        doc="The radius property")
