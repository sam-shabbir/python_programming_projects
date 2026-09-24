import random

user_wins = 0
computer_wins = 0

# store the list in a variable
options = ["rock", "paper", "scissors"]
# variable =  list

while True: # while loop
    user_input =  input ("Type : Rock/Paper/Scissors or Q to quit:  ").lower() # to convert users input to lower case
    if user_input == "q":
        break # i.e end the programme

    if user_input not in options: # list is denotaed by " " within a []
        continue

# if their input is valid we generate a number between 0 & 2
    random_number = random.randint (0, 2)
    # rock: 0 , paper: 1 & scissors: 2

    computer_pick = options [random_number]
    print ("Computer picked",  computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors": 
        print ("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print ("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print ("You won!")
        user_wins += 1

    elif user_input == computer_pick:
        print("You and the computer tied!")
        continue
    
    else:
        print("You lost! :( )")
        computer_wins +=1

    # print out no of user wins Vs Comp wins

print("You win",  user_wins, "times." )
print("The computer win",  computer_wins, "times." )

print ("Goodbye")