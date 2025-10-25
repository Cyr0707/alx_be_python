import math

class Shape:
    """
    Base class representing a generic shape.
    Demonstrates polymorphism by defining an area method
    meant to be overridden by subclasses.
    """
    def area(self):
        """
        Calculates the area of the shape.
        Should be overridden in derived classes.
        """
        raise NotImplementedError("Subclasses must implement this method")


class Rectangle(Shape):
    """
    Represents a rectangle.
    Inherits from Shape and overrides the area() method.
    """
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    """
    Represents a circle.
    Inherits from Shape and overrides the area() method.
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
