#6 - PIG (Medium)

import random

def roll(): #function
    min_value = 1
    max_value = 6

    roll = random.randint(min_value, max_value)

    return roll

while True: # loop until valid input
    players = input ("Enter the no of players (2 - 4): ")
    if players.isdigit(): # to check if the input is a number
        players = int(players) # convert to integer so that we can compare it with the range

        if 2 <= players <=4:
            break # valid input, exit the loop

        else:
            print("MUST BE a number between 2 to 4 players.")

    else:
        print("Invalid, Please try again.")

max_score = 50
player_scores = [0 for _ in range (players)] # initialize player scores to 0, the length of the list is equal to the number of players

while max (player_scores) < max_score: # loop until a player reaches the max score

    for player_idx in range(players): # loop through each player
        print("\n Player number", player_idx +1, " turn has just started!\n") # print the current player's turn
        # \n adds a new line break for better readability

        print("Your total score is: ", player_scores[player_idx], "\n") # print the current player's total score

        current_score = 0 # initialise current score for turn to 0

        while True:
            should_roll = input ("Would you like to roll? (y/n): ").lower() # ask the player if they want to roll, convert to lowercase for easier comparison")

            if should_roll .lower() != "y":
                break

            value = roll() # call the roll function to get a random number between 1 and 6
            if value ==1: # if the player rolls a 1, their turn is over and they lose all points for that turn
                print("You rolled a 1! Your turn is over and you lose all points for this turn.")
                current_score = 0
                break

            else:
                current_score += value # add the value rolled to the current score
                print("You rolled a: ", value) # print the value rolled
            
            print("Your current score is: ", current_score)

        # FIX: these two lines were indented one level too little, so they ran only
        # AFTER every player had gone - only the last player's points were ever saved.
        # Indenting them inside the `for` loop adds each player's points after their own turn.
        player_scores[player_idx] += current_score
        print("your total score is: ", player_scores[player_idx])

max_score = max(player_scores) # get the maximum score among all players
winning_idx = player_scores.index(max_score) # get the index of the player with the maximum score

# FIX: the original string was split across two lines with the quotes in the wrong places (SyntaxError)
print("Player number", winning_idx + 1, "is the winner with a score of:", max_score)