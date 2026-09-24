# Problem 35 - Digit Detection in Strings
"""
Practice Problem: Write a program to check if a user-entered string contains any numeric digits. Use a for loop to examine each character.

Exercise Purpose: This exercise will help you learn about string traversal and character analysis.
In software development, these skills are important for tasks like checking if a username has forbidden characters or if a password is complex enough.

Given Input: input_string = "Python3"
"""

user_input = "Python3"
contains_digit = False

# Iterate through each character
for char in user_input:
    if char.isdigit():
        contains_digit = True
        break  # Exit early since we found one

print(f"The string '{user_input}' contains digits: {contains_digit}")

"""
Explanation to Solution:

Flag Pattern: We initialize contains_digit as False. This “flag” only flips if a specific condition is met.
.isdigit(): This character method returns True if the character is a numeric value (0-9) and False otherwise.
break: This keyword is an efficiency tool. Once a single digit is found, there is no need to check the remaining characters, saving processing time.
"""