# Quiz Game
print ("Welcome to the Quiz Game")

score = 0

# Question 1
print ("Question 1: What is the capital of France?")
print ("a) Berlin")
print ("b) Madrid")
print ("c) Paris")

answer1 = input ("Your answer: ")

if answer1 == "c":
    print ("Correct!")
    score += 1 # Increment the score by 1 if the answer is correct
else:
    print ("Incorrect!")


# Question 2
print ("Question 2: What is the largest planet in our solar system?")
print ("a) Jupiter")
print ("b) Saturn")
print ("c) Neptune")

answer2 = input("Your answer: ")

if answer2 == "a":
    print ("Correct!")
    score += 1 # Increment the score by 1 if the answer is correct
else:
    print ("Incorrect!")

# Question 3
print ("Question 3: What is the smallest country in the world?")
print ("a) Monaco")
print ("b) Vatican City")
print ("c) San Marino")

answer3 = input("Your answer: ")

if answer3 == "b":
    print ("Correct!")
    score += 1 # Increment the score by 1 if the answer is correct
else:
    print ("Incorrect!")

# Question 4
print ("Question 4: What is the capital of Japan?")
print ("a) Seoul")
print ("b) Beijing")
print ("c) Tokyo")

answer4 = input("Your answer: ")

if answer4 == "c":
    print ("Correct!")
    score += 1 # Increment the score by 1 if the answer is correct
else:
    print ("Incorrect!")

# Question 5
print ("Question 5: What is the largest ocean on Earth?")
print ("a) Atlantic Ocean")
print ("b) Indian Ocean")
print ("c) Pacific Ocean")

answer5 = input("Your answer: ")

if answer5 == "c":
    print ("Correct!")
    score += 1 # Increment the score by 1 if the answer is correct
else:
    print ("Incorrect!")

# Final Score
print (f"Your final score is: {score}/5") 
# Display the final score out of 5 to the user using an f-string to include the value of the score variable in the output string.  
# Each time the user answers a question correctly, we increment the score by 1 using the += operator. At the end of the game, we display the final score to the user. 
# Why f string? It allows us to easily include the value of the score variable in the output string without needing to concatenate strings or convert the score to a string. 
