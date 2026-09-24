#Choose your own adventure game

name = input("Type your name: ") 

print("Welcome" , name , "to this adventure!.") # string

answer = input ("You are on a dirt road, it has come to an end and you can go Left or Right , " \
"which way do you want to go? Type left or right:   ").lower()

if answer == "left":
    answer = input ("You have come to a river, you can walk around it or swim across, - " \
    "What do you want to do? Type Walk or Swim:  ")

    if answer == "swim":
        print ("You swam across and were eaten by an alligator")

    elif answer == "walk":
        print ("You walked for many miles, you ran out of water and you lost the game")

    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = input ("You have come to a bridge, it looks wobbly, do you want to go cross it still or head back (cross / back)?.")

    if answer == "back":
        print ("You go back and loose.")

    elif answer == "cross":
        answer = input ("You cross the bridge and meet a stranger, Do you want to talk to them? Type yes or no")
        
        if answer == "yes":
            print ("You spoke to a stranger and they give you gold. You WIN.")

        elif answer == "no":
            print ("You ignored the stranger and they are offended and they have killed you. You Loose.")
        
        else:
            print ("Not a valid option. You loose!.")
        
    else:
        print("Not a valid option. You loose!.")
                   
else:
    print ("Not a valid option. You loose!.")

print ("Thank you for trying, better luck next time." , name)