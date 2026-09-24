# Problem 18 - Integer Digit Extraction and Reversal
"""
Practice Problem: Write a program to extract each digit from an integer in the reverse order.

Exercise Purpose: This exercise explores “Mathematical Parsing.” Instead of converting a number to a string, use the modulo operator (%) and floor division (//) to isolate digits.
This is common in low-level programming and algorithm challenges where type conversion is restricted.
Given Input: number = 7536
"""
number = 7536
print("Given Number:", number)

while number > 0:
    # Get the last digit
    digit = number % 10
    
    # Remove the last digit from number
    number = number // 10
    
    print(digit, end=" ")

"""
Explanation to Solution:

number % 10: This operation returns the remainder of the number divided by 10, which is always the rightmost digit.
number // 10: Floor division removes the decimal part, effectively shifting the number one decimal place to the right.
end=" ": This keeps the output on a single line, separated by spaces, rather than printing each digit on a new line.
"""
