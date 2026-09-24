# 8 - Timed math challenge
import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 10
TOTAL_PROBLEMS = 10


def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)
    
    expr = str(left) + " " + operator + " " + str(right)
    # print(expr)
    answer = eval(expr)

    return expr, answer

# generate_problem()
# expr, answer = generate_problem()
# print (expr, answer)

wrong = 0
input("Press enter to start")
print ("---------------------------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i+1) + ": " + expr + " = ") # WHY is there a # in code?
        if guess == str(answer): # need to convert answer to string to compare with guess so as to allow it for the same type
            break
        wrong += 1
        print("Wrong! Try again.")

end_time = time.time()
total_time = round(end_time - start_time, 2)

print ("---------------------------------------")
print ("Nice work!, you finished in ", total_time, " seconds!", "You had ", wrong, "wrong answers.")