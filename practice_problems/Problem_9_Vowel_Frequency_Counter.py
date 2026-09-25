# Exercise 9. Vowel Frequency Counter
"""

Practice Problem: Write a program to count the total number of vowels (a, e, i, o, u) present in a given sentence.

Exercise Purpose: This exercise introduces “Membership Testing".
By checking if a character belongs to a specific group (the vowels), you learn how to filter data based on categories. This is a fundamental step toward building text-analysis tools or spam filters.

Given Input: sentence = "Learning Python is fun!"

Expected Output: Number of vowels: 6
"""
# Input Sentence
sentence = "Learning Python is fun!"  # FIX: don't name a variable `input` - it hides Python's built-in input() function
vowel_letters = "aeiou"  # FIX: was "a e i o u" - the spaces counted as "vowels", so it printed 9 instead of 6
count = 0

# Count vowels from input
for char in sentence.lower():
    if char in vowel_letters:
        count +=1

# print no of vowels
print(f"No. of Vowels in input are: {count}")

