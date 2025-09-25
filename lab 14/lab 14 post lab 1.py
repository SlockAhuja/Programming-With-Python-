# AHuja slock

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


# Example usage
circle1 = Circle(7)

print("=== Circle Details ===")
print(f"Radius: {circle1.radius}")
print(f"Area: {circle1.area():.2f}")
print(f"Perimeter: {circle1.perimeter():.2f}")
