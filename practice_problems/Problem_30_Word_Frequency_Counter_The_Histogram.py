# Exercise 30. Word Frequency Counter (The Histogram)
"""
Practice Problem: Write a program that counts how many times each word appears in a given paragraph and stores these counts in a dictionary.

Exercise Purpose: This is a classic “Natural Language Processing” (NLP) task.
It teaches you how to map data to occurrences, which is the logic used by search engines to index web pages or by social media platforms to identify trending hashtags.

Given Input: text = "apple banana apple cherry banana apple"
"""
text = "apple banana apple cherry banana apple"

words = text.split()
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print(frequency)

"""
Explanation to Solution:

.split(): This breaks the string into a list of individual strings, allowing us to process them one by one.
Dictionary Membership: if word in frequency checks if the word has already been “seen” by the script.
Incrementing Values: By using the word as a key and the count as a value, we create a high-speed lookup table of the paragraphs content.
"""