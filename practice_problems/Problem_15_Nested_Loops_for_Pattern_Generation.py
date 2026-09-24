# Exercise 15. Nested Loops for Pattern Generation

"""
Practice Problem: Print the following pattern where each row contains a number repeated a specific number of times based on its value.

1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5

Exercise Purpose: Pattern printing is a classic way to learn “Nested Loops”.
You coordinate an outer loop for rows and an inner loop for columns or repetitions.
This improves spatial logic and control over output formatting.

Given Input: Range: 1 to 5

"""
# Outer loop for rows
for num in range(1, 6):
   
    # Inner loop for repetition
    for i in range(num):
        print(num, end=" ") # end=" " keeps it on the same line
    
    # New line after each row
    print("\n")

"""
Explanation to Solution:

Notice that each row contains the same number repeated, and the number of repetitions increases with the row number.

Nested Loops: The outer loop num sets the “context” for the row. The inner loop i performs the work for that specific row.
end=" ": By default, print() adds a newline. Overriding this with a space allows multiple numbers to appear side-by-side.
Formatting: The final print("\n") acts as a “carriage return,” starting the next row of the pattern on a clean line.

"""