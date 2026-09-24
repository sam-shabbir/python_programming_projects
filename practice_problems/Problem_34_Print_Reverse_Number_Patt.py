# Problem 34 - Print Reverse Number Pattern
"""
Practice Problem: Print a downward number pattern where each row starts with a decreasing value.

Exercise Purpose: In this exercise, you will learn about range control and practice using negative steps in loops to move backwards.
This skill is important for algorithms that process data from the end of a file to the beginning.

Given Input: Rows = 5
"""
rows = 5
# Outer loop for number of rows
for i in range(rows, 0, -1): # why 0 & -1? 
    # Inner loop for printing numbers in each row
    for j in range(i, 0, -1): 
        print(j, end=' ')
    print("") # New line - why not \n? for new line?

"""
Explanation to Solution:

range(rows, 0, -1): The -1 argument is the step. It tells Python to count backwards.
print(j, end=' '): By overriding the default newline with a space, we keep the numbers on the same horizontal line.
print(""): This simple empty print statement acts as a “carriage return” to start the next row of the pattern.
"""