# Exercise 14. Substring Frequency Analysis
"""
Practice Problem: Write a program to find how many times the substring “Emma” appears in a given string.

Exercise Purpose: Text analysis and pattern matching are core pillars of programming.
This exercise introduces searching for a “needle in a haystack,” a fundamental concept for building search engines or data validation tools.

Given Input:

str_x = "Emma is good developer. Emma is a writer"
"""
str_x = "Emma is good developer. Emma is a writer"

# find word & print how many times "Emma" appears in the string.
count = str_x.count("Emma")
print(f"Emma appeared {count} times")

"""
str_x.count("Emma"): This is a high-level abstraction that handles the complex logic of scanning the string and incrementing a counter internally.
Case Sensitivity: Note that string methods like count are case-sensitive; searching for “emma” (lowercase) would return 0.
"""

