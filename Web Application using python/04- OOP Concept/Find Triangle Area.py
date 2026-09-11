#find the area of a triangle using OOP concept

import math

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b 
        self.c = c 
    
    def area(self):
        s = (self.a + self.b + self.c) / 2
        area = math.sqrt(s * (s- self.a) * (s - self.b) * (s - self.c))
        print(f"The area of the triangle is: {area}")
        
#object creation
obj = Triangle(3, 4, 5)
obj.area()