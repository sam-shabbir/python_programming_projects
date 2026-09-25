import random

COLORS =  ["R", "G", "B", "Y", "W", "O"] # in capitals because it is a constant
TRIES = 10
CODE_LENGTH = 4

def generate_code ():
    code = []

    for _ in range (CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)
    
    return code

# guess code

def guess_code():

    while True:
        # FIX: was .split("  ") (two spaces), so "R G B Y" never split into 4 parts.
        # .split() with no argument splits on any amount of whitespace.
        guess = input("Guess (e.g. R G B Y): ").upper().split()

        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors.") # FIX: added the missing f so {CODE_LENGTH} shows the number
            continue
        
        for color in guess:
            if color not in COLORS:
                print(f"Invalid color: {color}. Try again!")
                break
        else:
            break
    
    return guess

def check_code(guess, real_code):
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1

    # zip() pairs items up by position: zip(["R","G"], ["R","B"]) -> ("R","R"), ("G","B")
    for guess_color, real_color in zip(guess, real_code): # FIX: second argument was real_color (not defined yet) - it should be the code list
        if guess_color == real_color:
            correct_pos +=1 # +1 because we found one more peg in exactly the right place
            color_counts[guess_color] -= 1 # substract the matches

    for guess_color, real_color in zip (guess, real_code): # FIX: same as above
        # FIX: skip pegs already counted as correct - otherwise a correct peg could be counted twice
        if guess_color == real_color:
            continue
        if guess_color in color_counts and color_counts[guess_color] > 0: # if the key exists and is greater than 0
            incorrect_pos += 1
            color_counts[guess_color] -=1 # FIX: was guess+color (a typo for guess_color)

    return correct_pos, incorrect_pos

def game():
    print(f"Welcome to mastermind, you have {TRIES} tries to guess the code...")
    print("The valid colors are", *COLORS) # *COLORS will have all the colors

    code = generate_code()
    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code) # FIX: was check_pos - the function is called check_code

        if correct_pos == CODE_LENGTH:
            print(f"You guessed the code in {attempts} tries!")
            break

        print (f"Correct Positions: {correct_pos} | Incorrect Positions: {incorrect_pos}")
               
    else:
        print("You ran out of tries, the code was:", *code) # why *code? 
              
if __name__ == "__main__":
    game()




