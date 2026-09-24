# Problem 32. Dictionary of Squares (Mapping Logic)
"""
Practice Problem: Create a dictionary where the keys are numbers from 1 to 10 and the values are the squares of those numbers (e.g., 2: 4, 3: 9).

Exercise Purpose: This exercise explores “Data Mapping.” It demonstrates how dictionaries can be used to store pre-calculated mathematical relationships, essentially acting as a “lookup table” that can replace expensive repetitive calculations.

Given Input: Range: 1 to 10
"""
squares = {}

for i in range(1 , 11):
    squares[i] = i * i
print(squares)

"""
Explanation to Solution:

range(1, 11): This provides the “keys” for our dictionary.
i * i: This calculates the square of the current number.
Key-Value Assignment: The line squares[i] = i * i creates a permanent link between the input number and its squared result within the dictionary structure.
"""
    
