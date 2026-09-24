# Exercise 13. Filtering Lists with Conditional Logic
"""
Practice Problem: Iterate through a given list of numbers and print only those numbers which are divisible by 5.

Exercise Purpose: This exercise teaches the use of the modulo operator (%) and loop filtering. In data processing, you often need to sift through large datasets to extract subsets that meet mathematical criteria.

Given Input: num_list = [10, 20, 33, 46, 55]
"""
num_list = [10, 20, 33, 46, 55]
print("Given list is", num_list)
print("Numbers divisible by 5 in the list are: ")

# Iterate through each element
for num in num_list:
    # Check divisibility
    if num % 5 == 0:
        print(num)

"""
Explanation to Solution:

for num in num_list: This construct allows the program to visit every item in the collection without needing to track indices manually.
num % 5 == 0: The modulo operator returns the remainder. If the remainder of division by 5 is 0, the number is a multiple of 5.
Filtering Logic: Only when the if condition evaluates to True does the print function execute, effectively “filtering” the list.

"""