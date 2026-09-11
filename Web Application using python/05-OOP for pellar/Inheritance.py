#Super class

class Father:
    def land(self):
        print("Father has 2 acres of land")
#Sub class
class Son(Father):
    def bike(self):
        print("Son has a bike")
#Sub class object creation
myson = Son()

# sub class can access the method of super class
myson.bike() #Son class method
myson.land() #Father class method


# Parent class
class Animal:
    def eat(self):
        print("Animal can eat")

# Child class
class Dog(Animal):
    def bark(self):
        print("Dog can bark")

# Object creation
mydog = Dog()

mydog.eat()  # Inherited method
mydog.bark()  # Child class method