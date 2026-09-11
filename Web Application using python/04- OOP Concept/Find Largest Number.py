#find the largest number using OOP concept

class Number:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def find_largest(self):
        if self.a >= self.b and self.a >= self.c:
            print(f"{self.a} is the largest number.")
        elif self.b >= self.a and self.b >= self.c:
            print(f"{self.b} is the largest number.")
        else:
            print(f"{self.c} is the largest number.")   


#object creation
obj = Number(10, 20, 30)

obj.find_largest()