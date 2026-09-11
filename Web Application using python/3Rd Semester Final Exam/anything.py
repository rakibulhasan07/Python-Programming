# class Animal:                         # Super Class
#     def __init__(self, name):
#         self.__name = name             # Encapsulation

#     def get_name(self):
#         return self.__name


# class Turtle(Animal):                 # Sub Class
#     def run(self):                     # Polymorphism
#         print(self.get_name(), "is running slowly!")


# class Horse(Animal):                  # Sub Class
#     def run(self):                     # Polymorphism
#         print(self.get_name(), "is running fast!")


# turtle = Turtle("Tim")
# horse = Horse("Harry")

# turtle.run()
# horse.run()

class animal:   # Super Class       
    def __init__(self, name):
        self.__name = name      # Encapsulation

    def get_name(self):
        return self.__name

class Turtle(animal):  # Sub Class
    def run(self):  # Polymorphism
        print(self.get_name(), "is running slowly!")

class Horse(animal):  # Sub Class
    def run(self):  # Polymorphism
        print(self.get_name(), "is running fast!")
turtle = Turtle("Tim")
horse = Horse("Harry")

turtle.run()
horse.run()
