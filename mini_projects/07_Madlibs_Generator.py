#7 - Madlibs Generator (Medium)

with open ("story.txt", "r") as f: # FIX: was "story.txt1" - no file with that exact name existed #file in .txt format
    story = f.read() # read the contents of the file and store it in a variable called story

# print(story)
words = set() # set to store unique o
start_of_word = -1 #variable to store the index of the start of a word
# why -1? because we will check if it has been updated when we find the end of the word. If it is still -1, it means we have not found the start of a word yet.

target_start = "<"
target_end = ">"

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i
    
    if char == target_end and start_of_word != -1: # check if we have found the end of a word and if we have found the start of a word before. 
        # If start_of_word is still -1, it means we have not found the start of a word yet, so we cannot extract the word.
        word = story [start_of_word: i +1] # extract the word from the story using slicing. We add 1 to i to include the target_end character in the word.
        # why i+1 because slicing in python is exclusive of the end index, so we need to add 1 to include the target_end character in the word.
        words.add(word)
        start_of_word = -1 

# print(words)

answers = {} # dictionary to store the answers for each word ie key = value. WHY and empty dictionary? because we will fill it with the answers from the user

for word in words:
    answer = input ("Enter a word for " + word + ": ") # cancathenate the word with the prompt
    # FIX: was ("Enter a word for" , + word + ": ") - the comma made it two arguments (input() only takes one)
    # and `+ word` on its own tried to make a string "positive", which is a TypeError
    answers[word] = answer # store the answer in the dictionary with the word as the key

# print(answers)

for word in words:
    story =story.replace(word, answers[word]) # replace the word in the story with the answer from the user. 
    # We use the replace method of the string to replace all occurrences of the word in the story with the answer from the user.

print (story)

