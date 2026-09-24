# Problem 21 - Downward Half-Pyramid Pattern
"""
Practice Problem: Print a downward half-pyramid pattern using stars (*).

Exercise Purpose: Learn about reverse indexing. Controlling loop boundaries in reverse is important for algorithms that process data from end to beginning.

Given Input: Rows: 5

Expected Output:

* * * * * 
* * * * 
* * * 
* * 
*
"""

# Loop from 5 down to 1
for i in range(5, 0, -1):
    for j in range(0, i):
        print("*", end=" ")
    print("\n")

"""
Explanation to Solution:

range(5, 0, -1): The third argument -1 is the “step.” It tells the loop to decrement the value of i in each iteration.
String Multiplication (Alternative): In Python, you could also write print("* " * i), which is a more concise “Pythonic” way to repeat characters.
Inner Loop Constraint: The inner loop’s range is bound by the current value of the outer loop, causing the line length to decrease over time.
"""