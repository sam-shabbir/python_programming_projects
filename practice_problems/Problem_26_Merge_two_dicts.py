# Exercise 26. Merging Two Dictionaries
"""
Practice Problem: Write a program that takes two separate dictionaries and merges them into one single dictionary.

Exercise Purpose: This introduces “Key-Value Consolidation.” Merging dictionaries is a common task when combining configuration files or user profiles.
It also teaches you about “Key Overwriting” — what happens when both dictionaries share the same key.

Given Input:

dict1 = {"name": "Alice", "age": 25}
dict2 = {"city": "New York", "job": "Engineer"}
"""

dict1 = {"name": "Alice", "age": 25}
dict2 = {"city": "New York", "job": "Engineer"}

# Modern Python merge (Union Operator)
merged_dict = dict1 | dict2 # | is the merge operator

print(merged_dict)

"""
Explanation to Solution:

The | Operator: This creates a new dictionary containing the keys and values of both inputs.
Conflict Resolution: If both dictionaries had an “age” key, the value from the second dictionary (dict2) would prevail in the final merge.
Immutability: This method preserves the original dict1 and dict2 while creating a third, combined object.
"""