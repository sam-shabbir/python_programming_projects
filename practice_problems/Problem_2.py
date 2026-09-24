# Exercise 2. Cumulative Sum of a Range
# Practice Problem: Iterate through the first 10 numbers (0–9). In each iteration, print the current number, the previous number, and their sum.

# Exercise Purpose: This exercise teaches “State Tracking.” In programming, you often need to remember a value from a previous loop iteration to calculate results in the current one.
# This is the basis for algorithms like Fibonacci sequences or running totals.

"""
Given Input: Range: numbers = range(10)

Expected Output:

Printing current and previous number sum in a range(10)
Current Number 0 Previous Number 0 Sum: 0
Current Number 1 Previous Number 0 Sum: 1
Current Number 2 Previous Number 1 Sum: 3
....
Current Number 8 Previous Number 7 Sum: 15
Current Number 9 Previous Number 8 Sum: 17
"""

print("Printing current and previous number sum in a range(10)")
previous_num = 0

# Loop from 0 to 9
for i in range(10):
    x_sum = previous_num + i
    print(f"Current Number {i} Previous Number {previous_num} Sum: {x_sum}") # added text and 3 x {} variables. 
    
    # Update previous_num for the next iteration
    previous_num = i