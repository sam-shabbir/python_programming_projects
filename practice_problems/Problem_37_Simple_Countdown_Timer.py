# Problem 37 - Simple Countdown Timer
"""
Practice Problem: Create a countdown timer that starts from a given number and counts down to zero using a while loop.

Exercise Purpose: In this exercise, you will learn about loop termination logic and time delay management.
Knowing how to control the flow of your code in real time is important for making animations, game loops, or automated scripts.

Given Input: start_count = 5
"""
import time

count = 5

while count > 0:
    print(count)
    # Pause the program for 1 second
    time.sleep(1)
    # Decrement the counter
    count -= 1

print("Blast off!")

"""
Explanation to Solution:

while count > 0: This condition ensures the loop runs exactly as many times as specified. Once count hits 0, the condition becomes False and the loop stops.
time.sleep(1): This function from the time module pauses execution for one second, making the output feel like a real clock.
count -= 1: This is shorthand for count = count - 1. Without this line, the loop would be “infinite” because count would always stay at 5.
"""