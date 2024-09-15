import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

radius = Circle(5)

print(f"Area of the circle: {radius.area():.2f}")
print(f"Perimeter of the circle: {radius.perimeter():.2f}")
