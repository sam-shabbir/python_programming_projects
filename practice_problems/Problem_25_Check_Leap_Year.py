# Problem 25 - Check Leap Year

"""
Practice Problem: Write a program that takes a year as input and determines if it is a leap year.

A leap year is a year in the Gregorian calendar that contains an extra day, making it 366 days long instead of the usual 365.
This extra day, February 29th, is added to keep the calendar synchronized with the Earths revolution around the Sun.

Rules for leap years: a year is a leap year if its divisible by 4, unless its also divisible by 100 but not by 400.

Exercise Purpose: This exercise is vital for mastering “Complex Conditional Logic.” A leap year isnt just “every 4 years”; there are specific exceptions for century years.
This forces the programmer to use nested if statements or compound logical operators (and/or).

Given Input: year = 2024
"""

def is_leap(year): 
    # Standard Leap Year Logic
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

is_leap(2024)
is_leap(2100)

""" Explanation to Solution:

year % 4 == 0: Checks the basic 4-year cycle.
year % 100 != 0: Excludes years like 1900 or 2100, which are divisible by 4 but are not leap years.
or (year % 400 == 0): The “exception to the exception,” ensuring years like 2000 are correctly identified as leap years."""
