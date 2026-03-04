# ax^2 + bx + c = 0

import math 
 
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
d = b**2 - 4*a*c
if d > 0:
   
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    print(x1, x2)
elif d == 0:
    d = b**2 - 4*a*c
    x = -b / (2*a)
    print(x)
else:
    print("No real roots")

    b 

    import math

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

d = b*b - 4*a*c

if d > 0:
    print((-b + math.sqrt(d)) / (2*a), (-b - math.sqrt(d)) / (2*a))
elif d == 0:
    print(-b / (2*a))
else:
    print("No real roots")
