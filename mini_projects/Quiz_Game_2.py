print("Welcome to my computer quiz") #print a specified value, marked with single or double
# "" '' or known as a string

playing = input("Do you want to play? ") # Playing is the variable that stores the user input
# input() is a built-in function that allows user to input something as a prompt
# prompt is a message that is displayed to the user to indicate what kind of input is expected
# and appears before the user starts typing.
# add space after the question mark to make it look better and its user friendly

if playing.lower() != "yes": # if statement is NOT equal to "yes"
    # .lower() is a built-in method that converts a string to lowercase letters
    quit() # quit is a built-in function that terminates the program
    # FIX: quit() was hidden inside a """string""", and the lines below were indented
    # by 2 and 3 spaces. Every line in the same block must use the SAME indentation (4 is the standard).

print("Okay! let's play:)") # if the user input is "yes" the program will continue
# FIX: these two lines moved OUT of the if-block - before, they only ran when the player said "no"
score = 0 # score is the variable that stores the user's score and is initialized to 0

# FIX: every answer is now compared with .lower() on both sides, so "CPU" answers are
# accepted whether typed as "Central Processing Unit" or "central processing unit"
answer = input ("What does CPU stand for? ") # answer is the variable that stores the user input
# the user is prompted to answer the question "What does CPU stand for?"
if answer.lower() == "central processing unit": # if statement is equal to "central processing unit"
    print("Correct!") # if the user input is correct, it will print "Correct!"
    score +=1 # score is incremented by 1 if the user input is correct
else: # else statement is used to execute a block of code if the condition in the if statement
      # is false
    print("Incorrect!") # if the user input is incorrect, it will print "Incorrect!"

answer = input ("What does GPU stand for? ") # answer is the variable that stores the user input
# the user is prompted to answer the question "What does GPU stand for?"
if answer.lower() == "graphics processing unit": # if statement is equal to "Graphics Processing Unit"
    print("Correct!") # if the user input is correct, it will print "Correct!"
    score +=1 # score is incremented by 1 if the user input is correct  
else: # else statement is used to execute a block of code if the condition in the if statement
      # is false
    print("Incorrect!") # if the user input is incorrect, it will print "Incorrect!"


answer = input ("What does RAM stand for? ") # answer is the variable that stores the user input
# the user is prompted to answer the question "What does RAM stand for?"
if answer.lower() == "random access memory": # if statement is equal to "Random Access Memory"
    print("Correct!") # if the user input is correct, it will print "Correct!"
    score +=1 # score is incremented by 1 if the user input is correct      
else: # else statement is used to execute a block of code if the condition in the if statement
      # is false
      # whenever colon is used the line next after it has to be indented

    print("Incorrect!") # if the user input is incorrect, it will print "Incorrect!"


answer = input ("What does PSU stand for? ") # answer is the variable that stores the user input
# the user is prompted to answer the question "What does PSU stand for?"
if answer.lower() == "power supply unit": # if statement is equal to "Power Supply Unit"
    print("Correct!") # if the user input is correct, it will print "Correct!"
    score +=1 # score is incremented by 1 if the user input is correct
else: # else statement is used to execute a block of code if the condition in the if statement
      # is false
    print("Incorrect!") # if the user input is incorrect, it will print "Incorrect!"

answer = input ("What does HDD stand for? ") # answer is the variable that stores the user input
# the user is prompted to answer the question "What does HDD stand for?"
if answer.lower() == "hard disk drive": # if statement is equal to "Hard Disk Drive"
    print("Correct!") # if the user input is correct, it will print "Correct!" 
    score +=1 # score is incremented by 1 if the user input is correct

else: # else statement is used to execute a block of code if the condition in the if statement
      # is false
    print("Incorrect!") # if the user input is incorrect, it will print "Incorrect!"   


print("You got " + str(score) + " questions correct!") # print the user's score
# str() is a built-in function that converts a value to a string

print("You got " + str((score/5)*100) + "%") # print the user's percentage score
# the percentage score is calculated by dividing the user's score by the total number of questions
# (5 in this case) and multiplying by 100 to get the percentage

