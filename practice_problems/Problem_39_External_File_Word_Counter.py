# Problem 39 - External File Word Counter
"""
Practice Problem: Write a script that opens an existing .txt file and counts the total number of words it contains.

Exercise Purpose: This exercise teaches “Data Parsing.” In professional environments, you rarely work with data you typed into the code yourself;
you almost always pull data from external sources. This script simulates basic text-mining techniques used to analyze documents or logs.

Given Input:

An external file sample.txt containing: “Coding is the language of the future.”
"""
# Assuming 'sample.txt' exists with some text
try:
    with open("sample.txt", "r") as file:
        data = file.read()
        words = data.split()
        word_count = len(words)
        print(f"The file contains {word_count} words.")
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")

"""
Explanation to Solution:

data.split(): By default, split() breaks a string at every space or newline. This effectively creates a list where every element is a single word.
len(words): Since words is now a list, the length of the list directly corresponds to the count of words in the document.
try-except: This is a bonus safety feature. If the file is missing, the program won’t “crash” with a scary error; instead, it will print a polite message explaining what happened.
"""