# Exercise 11. Removing Duplicates from a List
"""

Practice Problem: Write a script that takes a list containing duplicate items and returns a new list with only unique elements.

Exercise Purpose: This exercise teaches “Data De-duplication.”
In real-world data science, datasets are often “messy” with repeating entries. Mastering the conversion between Lists (which allow duplicates) and Sets (which do not) is the fastest way to clean data.

Given Input: data = [1, 2, 2, 3, 4, 4, 4, 5]

Expected Output: Unique List: [1, 2, 3, 4, 5]

"""
# input nums
input_nums = [1, 2, 2, 3, 4, 4, 4, 5]

# remove repeated nums
revised_nums = list(set(input_nums))

# print appended / refined / filtered list
print(f"Original List: {input_nums}")
print(F"Revised List is: {revised_nums}")

"""
Explanation to Solution:

set(data): A Set is a collection where every element must be unique. When you pass a list into a set, Python automatically discards any value it has already seen.
list(...): Since sets are unordered and do not support indexing, we convert the result back into a list so we can use it in standard list operations later.
Ordering Note: Converting to a set usually loses the original order of items. If order matters, you would need a loop or a dict.fromkeys() approach.

"""