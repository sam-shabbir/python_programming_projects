# Problem 40. Introduction to Classes (OOP)
"""
Practice Problem: Create a Car class with attributes for make, model, and year. Include a method called start_engine() that prints a formatted string describing the car starting up.

Exercise Purpose: This exercise introduces Object-Oriented Programming (OOP).
Instead of just writing functions, you are creating a “Blueprint” (the Class) to generate “Objects” (the specific cars).
This is how modern software is built, allowing you to organize code into logical, reusable components.

Given Input: Make: “Toyota”, Model: “Camry”, Year: 2022
"""
class Car:
    def __init__(self, make, model, year):
        # Setting up attributes
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        # A method that uses the object's attributes
        print(f"The {self.year} {self.make} {self.model}'s engine is now running!")

# Creating an object (an instance of the class)
my_car = Car("Toyota", "Camry", 2022)

# Calling the method
my_car.start_engine()

"""
Explanation to Solution:

__init__: This is the “Constructor.” It runs automatically the moment you create a new car, setting its identity (Toyota, Camry, etc.).
self: This is a placeholder for the specific object. It tells Python, “use this cars year” rather than just a generic variable named year.
Encapsulation: By grouping the data (attributes) and the actions (methods) together, your code becomes modular and much easier to manage as your program grows.
"""
