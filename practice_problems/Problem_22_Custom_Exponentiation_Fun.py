# Problem 22 - Custom Exponentiation Function
"""
Practice Problem: Write a function called exponent(base, exp) that returns an integer value of the base raised to the power of the exponent.

Exercise Purpose: Learn about “Accumulator Patterns.” Although Python has a built-in power operator (**),
making your own version shows how repeated multiplication works and how functions return results to the main program.

Given Input: base = 2, exp = 5

Expected Output: 2 raises to the power of 5: 32
"""
def exponent(base, exp):
    num = exp
    result = 1
    # Repeat multiplication 'exp' times
    while num > 0:
        result = result * base
        num = num - 1
    print(base, "raises to the power of", exp, "is:", result)

exponent(2, 5)
exponent(5, 4)
"""
Explanation to Solution:

Base Case: result starts at 1 because 1 is the identity element for multiplication (anything multiplied by 1 remains itself).
The while Loop: This controls the number of multiplications. Each cycle represents one “power.”
Function Reusability: By passing base and exp as parameters, the same block of code can calculate 25, 54, or any other combination.
"""