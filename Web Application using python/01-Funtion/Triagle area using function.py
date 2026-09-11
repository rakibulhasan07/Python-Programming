# Triangle area using function
def triangle_area():
    b = float(input("Enter the base of the triangle: "))
    h = float(input("Enter the height of the triangle: "))
    Area = 0.5 * b * h
    print("Area of the triangle is: ", Area)

triangle_area()

# Function to calculate triangle area
def triangle_area(base, height):
    area = 0.5 * base * height
    return area

# User input
base = float(input("Enter the base: "))
height = float(input("Enter the height: "))

# Function call
result = triangle_area(base, height)

# Output
print("Area of the triangle =", result)