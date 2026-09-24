# Exercise 12. List Comparison and Boolean Logic

"""
Practice Problem: Write a function to return True if the first and last number of a given list is the same. If the numbers are different, return False.

Exercise Purpose: This exercise introduces “Collection Indexing” and “Boolean Flags.” Comparing data structure boundaries is common in pattern matching and data integrity checks.

Given Input:

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

"""
def first_last_same(number_list):
    print("Given list:", number_list)
    
    first_num = number_list[0] # why is it 0?
    last_num = number_list[-1] # why is it -1 -- Python allows [-1] to represent the last item in a list regardless of the lists length. This is safer and cleaner than calculating len(list) - 1.
    
    if first_num == last_num:
        return True
    else:
        return False

numbers_x = [10, 20, 30, 40, 10]
print("result is", first_last_same(numbers_x))

numbers_y = [75, 65, 35, 75, 30]
print("result is", first_last_same(numbers_y))

"""
Explanation to Solution:

Negative Indexing: Python allows [-1] to represent the last item in a list regardless of the lists length. This is safer and cleaner than calculating len(list) - 1.
Equality Operator (==): This operator compares the values of the two objects and evaluates to a Boolean (True/False).
Logic Gate: The function provides a clear binary answer based on the structural properties of the input list.
"""