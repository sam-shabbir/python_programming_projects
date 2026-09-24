# Problem 33 - Character Replacer (Data Sanitization)
"""
Practice Problem: Ask the user for a sentence. Replace every empty space in that sentence with an underscore (_) and print the final result.

Exercise Purpose: This exercise focuses on “String Sanitization.” In web development and file management, spaces are often problematic (especially in URLs or file paths).
Learning to replace characters is a critical skill for preparing data for storage or transmission.

Given Input: "I love coding in Python"
"""

user_sentence = input("Enter a sentence: ")

# Replace space with underscore
sanitized_sentence = user_sentence.replace(" ", "_")

print(sanitized_sentence)