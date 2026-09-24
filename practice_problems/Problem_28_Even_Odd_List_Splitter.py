# Problem 28. Odd/Even List Splitter
"""
Practice Problem: Start with a list of 10 numbers. Iterate through them and sort them into two separate lists: one for even numbers and one for odd numbers.
"""
num_list = [12, 7, 34, 21, 5, 10, 8, 3, 19, 2]
even_nums = []
odd_nums = []

for num in num_list:
    if num % 2 == 0:
        even_nums.append(num)

    else:
        odd_nums.append(num)

print(f"Even numbers: {even_nums}")
print(f"Odd numbers: {odd_nums}")


"""
Explanation to Solution:

% 2 == 0: The modulo operator checks for a remainder. If a number divided by 2 has no remainder, it is mathematically even.
.append(): This method dynamically grows our target lists as the loop finds matching candidates.
Logical Branching: The if-else structure ensures that every number is placed in exactly one category, maintaining the integrity of the original dataset.
"""