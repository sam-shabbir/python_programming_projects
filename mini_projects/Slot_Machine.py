# deposit slot machine
import random

MAX_LINES = 3 # caps because it is a constant value whihc will not change
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbols_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = { # FIX: was misspelled `symnol_value`, so spin() hit a NameError looking up `symbol_value`
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            # FIX: this `else` belongs to the `for` loop, not the `if`.
            # A for-else runs only if the loop finished WITHOUT hitting `break`,
            # i.e. every column matched - so the player won this line (paid once, not once per column).
            winnings += values[symbol] * bet
            winning_lines.append (line + 1)
    return winnings, winning_lines # FIX: was indented inside the loop, so only the first line was ever checked

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = [] # list to store all the symbols based on the count provided in the symbols_count dictionary
    for symbol, symbol_count in symbols.items(): # .items method to give the key 
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = [] # lits of randomly generated columns for the slot machine
    for _ in range(cols):
        # why _ is used? 
        column = []
        current_symbols = all_symbols[:] # create a copy of the all_symbols list to keep track of the symbols that have been used in the current column - to copy : in []
        
        for _ in range(rows):
            value = random.choice(current_symbols) # randomly select a symbol from the current_symbols list
            current_symbols.remove(value) # remove the selected symbol from the current_symbols list to avoid duplicates in the same column
            column.append(value) # add the selected symbol to the current column
        columns.append(column)

    return columns
    
def print_slot_machine(columns):
    for row in range (len(columns[0])): # transposing operation for every row we look at every coloum
        for i, column in enumerate(columns):
            if i != len(columns) -1 : # maximum index we have to access in columns list
              print(column[row], end= " | ") # why end? **
            else:
                print (column[row], end= " ")
        print ()

def deposit():
    while True:
        amount = input("How much would you like to deposit? £")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a valid number.")
    return amount

def get_number_of_lines():
    while True:
        lines = input ("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Number of lines must be between 1 and 3.")
        else:
            print("Please enter a valid number.")
    return lines

def get_bet():
    while True:
        amount = input ("How much would you like to bet on each line? £")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between £{MIN_BET} - £{MAX_BET}.") # using f string to print the min and max bet values
        else:
            print("Please enter a valid number.")

    return amount # FIX: was amount() - the brackets tried to CALL the number like a function (TypeError: 'int' object is not callable)

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet *lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: £{balance}")
        else:
            break
    
    print(f"You are betting £{bet} on {lines} lines. Your total bet is: £{total_bet}.") # f string to print the bet, lines and total bet values

    slots = get_slot_machine_spin(ROWS, COLS, symbols_count)
    print_slot_machine(slots)

    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value) # the error here was the misspelled dictionary name at the top (symnol_value)
    print (f"You won: £{winnings}.")
    print(f"You have won on lines: ", *winning_lines)
    return winnings - total_bet

def main():
    
    balance = deposit ()
    while True:
        print (f"Current balance is: £{balance}")
        answer = input("Press enter to spin (q to quit).")
        if answer == "q": 
            break
        balance += spin(balance)

    print(f"You left with £{balance}")   

main()

