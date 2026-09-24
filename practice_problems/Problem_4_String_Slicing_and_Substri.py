# Problem 4 - String Slicing and Substring Removal
"""
Practice Problem: Write a function to remove characters from a string starting from index 0 up to n and return a new string.

Exercise Purpose: This exercise demonstrates how to truncate data strings, a common data-cleaning task.

Given Input:

remove_chars("pynative", 4) # every 4th
remove_chars("pynative", 2) # every 2nd

"""
word = "pynative"

def remove_chars(word, n): # from word at nth place
    print('Original string:', word)
    # Extract string from index n to the end
    res = word[n:]
    return res

print("Removing characters from a string")
print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))

"""
Explanation to Solution:

Slicing word[n:]: By omitting the “stop” value in the slice, Python defaults to the very end of the string.
Flexibility: The function is designed to take n as an argument, making it reusable for any length of removal.
Memory: Note that strings in Python are immutable; this function doesn’t change the original string but creates and returns a new truncated version.

"""