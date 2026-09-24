# Problem 27. Finding Common Elements (Intersections)
"""
 Practice Problem: Take two lists and find the elements that appear in both. Use Sets to perform the operation.

Exercise Purpose: This exercise explores “Mathematical Set Operations.” Finding intersections is vital for recommendation engines (e.g., finding “mutual friends” or “shared interests”).
It demonstrates why using the right data structure (Set) is more efficient than nested loops.

Given Input:

list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8] 
 
"""
list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8] 

set_a = set(list_a)
set_b = set(list_b)

# Find common elements using intersection
common = set_a & set_b

print(f"Common Elements: {common}")

"""
Explanation to Solution:

set_a & set_b: The ampersand represents the “Intersection” operation. It returns a set containing only items that are present in both set_a AND set_b.
Performance: Doing this with sets is significantly faster than using nested for loops, as set lookups are nearly instantaneous (O(1) average case).
Result Type: The output is a set {4, 5}, which effectively highlights that we are looking for a unique collection of shared items.
"""