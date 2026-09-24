# Problem 31 - Print Alternate Prime Numbers
"""
Write a program to find all prime numbers up to 20, but only print every second (alternate) prime number found.

Exercise Purpose: This exercise combines “Nested Loops” (to check for primality) with “Step Logic.”
It requires the programmer to first identify a subset of data and then apply a secondary filter, a common task in data reporting.

Given Input: Limit = 20

"""
prime_nums = []

for num in range(2, 21):
    # Check if number is prime
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            break
    else:
        prime_nums.append(num)

# Print alternate primes
alternate_primes = prime_nums[::2] # skips every other element
print(f"Alternate Prime Numbers are: " , alternate_primes)

"""
Explanation to Solution:

for...else loop: A unique Python feature where the else block executes only if the for loop completes without hitting a break. This is perfect for prime checking.
num**0.5: Efficiency trick — you only need to check factors up to the square root of a number.
primes[::2]: The slicing engine skips every other element in the list, fulfilling the “alternate” requirement
"""