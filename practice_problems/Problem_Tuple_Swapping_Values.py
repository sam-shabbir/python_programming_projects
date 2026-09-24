# Problem 5: Variable Swapping (The In-Place Method)

"""
Practice Problem: Write a program to swap the values of two variables, a and b, without using a third temporary variable.

Exercise Purpose: This exercise will help you learn about memory efficiency and Pythons special tuple unpacking feature.
In other languages like C or Java, you need a temporary variable to swap values safely.
In Python, you can swap values in one line without risking data loss.

Given Input: a = 5, b = 10
"""
# TUPLE 
# A tuple is an immutable object in Python that cannot be changed. Tuples are also sequences, just like Python lists.

a = 5
b = 10

print(f"Before Swap: a = {a} , b = {b}") 

#Swapping vlaues (New Tuple)
a, b = b, a

print(f"After Swap: a = {a}, b = {b}")