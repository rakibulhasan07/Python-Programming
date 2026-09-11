# Polymorphism Example
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Bird(Animal):
    def make_sound(self):
        return "Tweet!"

# Function demonstrating polymorphism
def animal_sounds(animals):
    for animal in animals:
        print(animal.make_sound())

# Object creation
dog = Dog()
cat = Cat()
bird = Bird()

# Calling the function with a list of different animal objects
animal_sounds([dog, cat, bird])


class Bird: 
    def Sound(self):
        print("Bird can make sound")

class Cat:
    def Sound(self):
        print('Cat says meow')

class Dog:
    def Sound(self):
        print('Dog says woof')

# ekoi Function Different Object a different kaj korchey
for animal in [Bird(), Cat(), Dog()]:
    animal.Sound()