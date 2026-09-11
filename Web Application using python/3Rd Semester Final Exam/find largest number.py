import cmath

class LargestNumberFinder:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def find_largest(self):
        if self.a >= self.b and self.a >= self.c:
            return self.a
        elif self.b >= self.a and self.b >= self.c:
            return self.b
        else:
            return self.c
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

largest_finder = LargestNumberFinder(num1, num2, num3)
largest_number = largest_finder.find_largest()
print("The largest number is:", largest_number)