# experiment on user-defined functions to calculate the area of a triangle
# Experiement No: 01
import math

def triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("Area of triangle is:", area)

a = float(input("Enter First Arm: "))
b = float(input("Enter Second Arm: "))
c = float(input("Enter Third Arm: "))

if a + b > c and a + c > b and b + c > a:
    triangle_area(a, b, c)
else:
    print("Triangle is not possible")


# agreement on user-defined functions to find the maximum of three values program
# Experiement No: 02
def max3val(a, b, c):
    if a>b and a>c:
        print("Maximum value is:", a)
    elif b>a and b>c:
        print("Maximum value is:", b)
    else:
        print("Maximum value is:", c)
a = float(input("Enter First Value: "))
b = float(input("Enter Second Value: "))
c = float(input("Enter Third Value: "))
max3val(a, b, c)




