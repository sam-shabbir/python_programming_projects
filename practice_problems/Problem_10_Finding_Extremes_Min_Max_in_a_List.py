# Exercise 10. Finding Extremes (Min/Max) in a List

"""
Practice Problem: Given a list of integers, find and print both the largest and the smallest numbers.

Exercise Purpose: This exercise explores “Aggregate Functions”. 
While Python has built-in tools for this, understanding how to identify extremes is critical for data normalization, where you often need to find the range of a dataset before processing it.

Given Input: nums = [45, 2, 89, 12, 7]

Expected Output: Largest: 89 Smallest: 2

"""
# input
input_nums = [45, 2, 89, 12, 7]

# find min & max
largest = max(input_nums)
smallest = min(input_nums)

# print min and max
print(f"Largest: {largest}")
print(f"Smallest: {smallest}")
