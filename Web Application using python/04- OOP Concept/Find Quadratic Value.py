# Find Quadratic Value Using OOP Concept

import math

class Quadratic:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def find_roots(self):
        d  = self.b ** 2 - 4 * self.a * self.c
        if d > 0:
            root1 = (-self.b + math.sqrt(d)) / (2 * self.a)
            root2 = (-self.b - math.sqrt(d)) / (2 * self.a)
            print(f"Two Real Roots: {root1} and {root2}")
        elif d == 0:
            root = -self.b / (2 * self.a)
            print(f"One Real Root: {root}")
        else:
            print("No Real Roots")

#object creation
obj = Quadratic(1, -5, 6)
obj.find_roots()