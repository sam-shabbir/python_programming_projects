# Turtle Racing
import turtle
import time
import random

WIDTH, HEIGHT = 500, 500 # for the display screen
COLORS = ["red",  "green", "blue", "orange", "yellow", "brown", "pink", "black", "purple", "cyan"] # FIX: "blue" and "orange" were listed twice, so two racers could share a color

def get_number_of_racers():
    racers = 0
    while True:
        racers = input ("Enter the no of racers (2 - 10):  ")
        if racers.isdigit(): # if string is a numeric
            racers = int(racers) # changes to integer
        else:
            print("input is not numeric. Try Again!")
            continue # goes back to the toop of the loop if Not Numeric

        if 2 <= racers <= 10:
            return racers
        else:
            print("Number not in range 2-10. Try Again!.. ")

def race(colors):
    turtles = create_turtles(colors)
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20) # randomly selects turtles to move at random speeds between 1 & 20
            racer.forward(distance)

            x, y = racer.pos() # to asses if crossed the finish line
            if y >= HEIGHT//2 - 10:
                return colors[turtles.index(racer)] # the color of the winning turtle - we will be given the index of the color of the winning turtle 
                # return colors[i] another way to do that 
                # when you return the function it stops the loop

def create_turtles(colors):
    turtles = [] # empty list
    spacingx = WIDTH // (len(colors) +1) # is it len of colors because we need to divide each color at at equal distance? **
    # enumerate() gives you the position (i) AND the item (color) on each loop - i is used below to space the turtles out
    for i, color in enumerate (colors): # FIX: loop variable was `colors`, overwriting the list we were looping over
        racer = turtle.Turtle()
        racer.color(color) # FIX: was racer.color(COLORS) - that passed the whole list, but each turtle needs ONE color
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos( -WIDTH//2 + (i + 1) * spacingx , -HEIGHT//2 + 20) # why is there i in it?**
        # i+1 becasue indexing starts at zero and we dont need 1st turtle at pos 0
        racer.pendown()
        turtles.append(racer)

    return turtles

def init_turtle(): # why INIT**
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing!") # FIX: title is a method you call, not a variable to assign

racers = get_number_of_racers()
init_turtle()

random.shuffle(COLORS)

colors = COLORS[:racers] # slice the number of colors we have = waht is this?**

winner = race(colors)
print("The turtle with the color:", winner, "has won the race!") # FIX: removed the stray `winner, +` (TypeError)
time.sleep (6)

# print(colors)