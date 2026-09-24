# Exercise 17. Merging Lists with Parity Filtering
"""
Practice Problem: Create a new list from two given lists such that the new list contains odd numbers from the first list and even numbers from the second list.
Given Input:
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
Expected Output: [25, 35, 40, 60, 90]
"""
def result_list(list1, list2):
    result_list = []
    
    # Get odd numbers from list1
    for num in list1:
        if num % 2 != 0:
            result_list.append(num)
            
    # Get even numbers from list2
    for num in list2:
        if num % 2 == 0:
            result_list.append(num)
            
    return result_list

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
print("result list:", result_list(list1, list2))
"""
Explanation to Solution:
result_list = []: Initializing an empty list is a standard pattern for gathering data dynamically.
num % 2 != 0: This checks for “not divisible by 2,” effectively finding odd numbers.
append(): This method adds elements to the end of the new list, preserving the order in which they were found in the source lists.
"""