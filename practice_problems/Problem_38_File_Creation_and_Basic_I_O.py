# Problem 38 - File Creation and Basic I/O
"""
Practice Problem: Write a program that creates a new text file named notes.txt, writes three separate lines of text to it, and then reads that file back to display the contents in the console.

Exercise Purpose: This exercise introduces “Persistent Storage.” Unlike variables that disappear when the program stops, 
files allow you to save data to the hard drive. Learning the open(), write(), and read() workflow is essential for building logging systems and saving user settings.

Given Input: Lines to write:

“Hello, this is my first note.”
“Python file handling is simple.”
“End of file.”
"""
# Part 1: Writing to the file
with open("notes.txt", "w") as file: # w is for write
    file.write("Hello, this is my first note.\n")
    file.write("Python file handling is simple.\n")
    file.write("End of file.\n")

# Part 2: Reading from the file
print("Reading file contents:")
with open("notes.txt", "r") as file: # r is for reading
    content = file.read()
    print(content)

"""
Explanation to Solution:

with open(...): Known as a “Context Manager,” this ensures that Python automatically closes the file even if an error occurs, preventing memory leaks or file corruption.
# \n: This is the “newline” character. Without it, all three sentences would be squashed together on a single line in the text file.
"w" vs "r": The mode "w" (Write) will overwrite the file if it already exists, while "r" (Read) opens it for viewing only.
"""