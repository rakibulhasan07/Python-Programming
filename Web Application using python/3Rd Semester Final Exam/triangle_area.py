### Function ব্যবহার করে ত্রিভুজের ক্ষেত্রফল নির্ণয়ের প্রোগ্রাম

# **সূত্র:**
# ত্রিভুজের ক্ষেত্রফল = `½ × ভূমি × উচ্চতা`


import datetime


def area(base, height):
    return 0.5 * base * height
try:
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    if b <= 0 or h <= 0:
        print("Invalid input! Please enter positive numbers for base and height.")
    else:
        print("Area of Triangle =", area(b, h))
except ValueError:
    print("Invalid input! Please enter valid numbers for base and height.")

current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print("Current Time:", current_time)

# ### Output

# ```text
# Enter base: 10
# Enter height: 5
# Area of Triangle = 25.0
# ```মনে রাখবে: def area() → Function তৈরি, আর area(b, h) → Function call। 

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

try:
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    if base <= 0 or height <= 0:
        print("Invalid input! Please enter positive numbers for base and height.")
    else:
        triangle = Triangle(base, height)
        print("Area of Triangle =", triangle.area())
except ValueError:
    print("Invalid input! Please enter valid numbers for base and height.")