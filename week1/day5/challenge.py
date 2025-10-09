# The goal is to create a class that represents a simple circle.
# A Circle can be defined by either specifying the radius or the diameter.
# The user can query the circle for either its radius or diameter.

# Other abilities of a Circle instance:

# Compute the circle’s area
# Print the attributes of the circle - use a dunder method
# Be able to add two circles together, and return a new circle with the new radius - use a dunder method
# Be able to compare two circles to see which is bigger, and return a Boolean - use a dunder method
# Be able to compare two circles and see if there are equal, and return a Boolean- use a dunder method
# Be able to put them in a list and sort them
# Bonus (not mandatory) : Install the Turtle module, and draw the sorted circles

import math

class Circle:
    def __init__(self, radius=0, diameter=None):
        if diameter is not None:
            self.radius = diameter / 2
        else:
            self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def area(self):
        return math.pi * (self.radius ** 2)

    def __str__(self):
        return f"Circle with radius {self.radius}"

    def __add__(self, other):
        return Circle(radius=self.radius + other.radius)

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius


# DEMO
if __name__ == "__main__":
    c1 = Circle(radius=3)
    c2 = Circle(diameter=10)

    print(c1)              
    print("c2 diameter:", c2.diameter)
    print("c1 area:", c1.area)

    c3 = c1 + c2
    print("c3 radius:", c3.radius)

    print("c1 == c2 ?", c1 == c2)
    print("c1 < c2 ?", c1 < c2)

    circles = [c2, c1, c3]
    print("Sorted:", sorted(circles))
