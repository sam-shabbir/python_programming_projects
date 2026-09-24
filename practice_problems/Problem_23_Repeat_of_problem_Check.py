# Problem 23 - Repeat of problem - Check Pelindrome Numbers

"""
Exercise 23. Check Palindrome Number
Practice Problem: Write a program to check if a given number is a palindrome. A palindrome number remains the same when its digits are reversed (e.g., 121, 545).

Exercise Purpose: This exercise teaches “Algorithmic Reversal.”
While strings are easy to reverse in Python, reversing a number mathematically using the modulo (%) and floor division (//) operators deepens understanding of how integers are stored in memory
and how to manipulate digits individually.

Given Input: number = 121
"""
def check_palindrome(number):
    # Convert to string to easily reverse
    str_num = str(number)
    reverse_str = str_num[::-1]
    
    if str_num == reverse_str:
        print(f"Original number {number}")
        print("Yes. given number is palindrome number")
    else:
        print(f"Original number {number}")
        print("No. given number is not palindrome number")

check_palindrome(121)

"""
Explanation to Solution:

str(number): Converts the integer into a sequence of characters so we can treat it like a list.
[::-1]: This is the slice notation for “start at the end, end at the beginning, and move backwards by 1.” It effectively mirrors the string.
if str_num == reverse_str: A boolean comparison that checks for exact symmetry.
"""