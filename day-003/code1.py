print("Welcome to the Treasure Islands. Your mission in this game is to find the treasure")
input("Hit Enter to start the game.")
left_or_right = input("Which side do you want to go (Left/Right) : ")
if(left_or_right == "right"):
    print("GAME OVER!!")
elif(left_or_right == "left"):
    swim_or_wait = input("Do you want to swim or wait: ")
    if (swim_or_wait == "swim"):
        print("GAME OVER!!")
    elif (swim_or_wait == "wait"):
        door = input("There are three doors, which door do you want to open (red/blue/yellow): ")
        if(door == "red" or door == "blue"):
            print("GAME OVER!!")
        elif(door == "yellow"):
            print("Congrats, you found the treasure and won the game! :3 :3")
        else:
            print("Please enter a valid input.")
    else:
        print("Please enter a valid input.")
else:
    print("Please enter a valid input.")