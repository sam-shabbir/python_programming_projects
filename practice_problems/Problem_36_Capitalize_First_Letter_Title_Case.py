# Problem 36 - Capitalize First Letter (Title Case)
"""
Practice Problem: Write a program to capitalize the first letter of each word in a given string without using the built-in .title() method.

Exercise Purpose: In this exercise, you will learn about “Tokenization” and “String Re-assembly.”
You will split a sentence into words, change them, and then put the sentence back together. This helps you practice working with complex data structures.

Given Input: text = "hello world from python"
"""
text = "hello world from python"

# Split the string into a list of words
words = text.split()
capitalized_words = []

for word in words:
    capitalized_words.append(word.capitalize())

    result =  " " . join(capitalized_words)
print(result)

"""
Explanation to Solution:

.split(): By default, this breaks a string into a list wherever there is a space. "hello world" becomes ["hello", "world"].
.capitalize(): This method turns the first character of a string to uppercase and the rest to lowercase.
" ".join(): This is the inverse of split. It takes a list and glues the items together using the string it is called on (in this case, a space) as the adhesive.
"""