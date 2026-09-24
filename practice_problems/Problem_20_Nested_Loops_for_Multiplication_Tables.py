# Problem 20 - Nested Loops for Multiplication Tables
"""
Practice Problem: Print a multiplication table from 1 to 10 in a formatted grid.

Exercise Purpose: To master “Matrix Generation.”
This builds on the nested loop concepts from Exercise 8 and applies them to generate a structured data table.
This is essential for understanding how to populate 2D arrays or generate spreadsheets.
Given Input: Range: 1 to 10
"""

for i in range(1, 11):
    for j in range(1, 11):
        # Print product followed by a tab space
        print(i * j, end="\t")
    print("\n")

"""
Explanation to Solution:

range(1, 11): Remember that Python’s range is exclusive of the stop value, so we use 11 to include 10.
\t (Tab Character): This is a string escape sequence that ensures the numbers align in neat columns regardless of whether they are one or two digits long.
Row/Column Coordination: For every iteration of the outer loop (i), the inner loop (j) completes a full cycle of 1 to 10.
"""