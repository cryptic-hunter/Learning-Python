#Hurdle 3
def turn_around():
    turn_left()
    turn_left()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    

while(at_goal() != True):
    if wall_in_front() is True:
        jump()
    else:
        move()