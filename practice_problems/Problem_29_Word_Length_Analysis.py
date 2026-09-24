# Exercise 29. Word Length Analysis
"""
Practice Problem: Create a list of 5 words. Write a loop that iterates through the list and prints each word alongside its character count.

Exercise Purpose: This exercise introduces “Metadata Extraction.” Often, you arent just interested in the data itself, but in its properties.
In web development, this logic is used to validate if a users password or username meets specific length requirements.

Given Input: words = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
"""
words = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

for word in words:
    length = len(word)
    print(f"{word} - {length}")

"""
Explanation to Solution:

len(): This is a universal Python function that returns the number of items in a sequence (in this case, characters in a string).
String Interpolation (f-strings): We use f"{word} - {length}" to create a clean, readable output format that combines variables and static text.
Sequential Processing: The loop ensures that the operation is performed on every item in the list automatically, regardless of how many words are added later.
"""