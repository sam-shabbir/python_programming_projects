# Problem 24 - Generate Fibonacci Series
"""
Practice Problem: Write a program to print the first 15 terms of the Fibonacci series. The sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding ones.

Exercise Purpose: The Fibonacci sequence is a classic way to learn about state management in loops.
You keep track of two changing variables at once to find the next number, which helps you see how data moves through each step.

Given Input: Terms = 15
"""
num1, num2 = 0, 1
print("Fibonacci series:")

for i in range(15):
    print(num1, end="  ")
    # Calculate next term
    res = num1 + num2
    # Update values for next iteration
    num1 = num2
    num2 = res
"""
Explanation to Solution:

num1, num2 = 0, 1: Pythons tuple unpacking allows for clean initialization of multiple variables.
res = num1 + num2: This creates the new term based on the current state of the two pointers.
num1 = num2 and num2 = res: This “shifts” the window forward by one position, preparing the variables for the next cycle. 
"""