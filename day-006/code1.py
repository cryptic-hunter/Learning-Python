#code blocks, indentations, functions, different for loops(while loops).

#Maze
#Partial Solution
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    
while not at_goal():
    while front_is_clear():
        move()
    while wall_in_front():
        while wall_on_right():
            turn_left()
        turn_right()


#Full Solution
def turn_right():
    turn_left()
    turn_left()
    turn_left()
        
while not at_goal():
    while front_is_clear():
        move()
        if right_is_clear() and front_is_clear():
            turn_right()
            move()
    while wall_in_front():
        while wall_on_right():
            turn_left()
        turn_right()