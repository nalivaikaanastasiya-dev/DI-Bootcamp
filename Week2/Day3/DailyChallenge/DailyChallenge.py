import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius 
        elif diameter is not None:
            self.diameter = diameter 
        else:
            raise ValueError("Must specify either radius or diameter.")

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive.")
        self._radius = value
    
    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, value):
        if value <= 0:
            raise ValueError("Diameter must be positive.")
        self._radius = value / 2

    def area(self):
        return math.pi * (self._radius ** 2)

    def __str__(self):
        return f"Circle (Radius: {self.radius:.2f}, Diameter: {self.diameter:.2f})"

    def __repr__(self):
        return f"Circle(radius={self.radius})"

    def __add__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        new_radius = self.radius + other.radius
        return Circle(radius=new_radius)

    def __gt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius > other.radius
    
    def __eq__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius == other.radius

    def __lt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius < other.radius

# --- Демонстрационная часть ---

print("--- Demonstration ---")

c1 = Circle(radius=4)
c2 = Circle(diameter=10)
c3 = Circle(radius=4)

print(f"\n1. Access and Area:")
print(f"C1: {c1}")
print(f"C2: {c2}")
print(f"C1 Area: {c1.area():.2f}")
c1.diameter = 12 
print(f"C1 Diameter set to 12. New Radius: {c1.radius}")

c_sum = c1 + c2
print(f"\n2. Addition (C1 + C2):")
print(f"({c1.radius} + {c2.radius}) = {c_sum.radius}")

print(f"\n3. Comparison:")
print(f"C1 == C3 (Radius 6 == 4)? {c1 == c3}") 
print(f"C1 > C2 (Radius 6 > 5)? {c1 > c2}")    

circles = [c_sum, c1, c2, c3]
print(f"\n4. Sorting (Unsorted Radii): {[c.radius for c in circles]}")
circles.sort() 
print(f"   Sorting (Sorted Radii):   {[c.radius for c in circles]}")
print(f"   Sorted List: {circles}")