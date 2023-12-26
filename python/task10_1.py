import math

class Shape:
    def area(self):
        pass  # Placeholder for the area method

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Example usage:
circle_instance = Circle(radius=5)
rectangle_instance = Rectangle(length=4, width=6)

print(f"Area of Circle: {circle_instance.area()}")
print(f"Area of Rectangle: {rectangle_instance.area()}")
