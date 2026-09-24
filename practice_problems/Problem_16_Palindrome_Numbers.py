# Exercise 16. Numerical Palindrome Check
"""
Practice Problem: Write a program to check if a given number is a palindrome (reads the same forwards and backwards).

Exercise Purpose: This exercise introduces the idea of “Reversing Logic”.
Reversing a string is simple, but reversing an integer takes some math, like using division and modulo, or changing its type. This shows how data types can work differently.

Given Input:

Case 1: number = 121
Case 2: number = 125
"""
def check_palindrome(number):
    print("original number", number)
    
    # Convert to string to reverse easily
    original_str = str(number)
    reversed_str = original_str[::-1]
    
    if original_str == reversed_str:
        print("Yes. given number is palindrome number")
    else:
        print("No. given number is not palindrome number")

check_palindrome(121)
check_palindrome(125)

"""
Explanation to Solution:

str(number): Type casting is used here to transform a math object into a sequence of characters.
[::-1]: This is the slice notation for reversing a sequence. It tells Python to step through the entire string backwards.
Boolean Comparison: The == operator determines if the two states (original vs. mirror) are identical.
"""