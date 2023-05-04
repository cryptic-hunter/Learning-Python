import random
from turtle import Turtle, Screen, forward


timmy_the_turtle = Turtle()
timmy_the_turtle.shape("classic")

####Draw a Square####
# def timmy_the_turtle_movement():
#     timmy_the_turtle.right(90)
#     timmy_the_turtle.forward(100)
# timmy_the_turtle.forward(100)
# timmy_the_turtle_movement()
# timmy_the_turtle_movement()
# timmy_the_turtle_movement()
# timmy_the_turtle.right(90)
##########################

####Draw a Dashed line####
# def dashed_line():
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.color("white")
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.color("black")
# def timmy_the_turtle_movement():
#     timmy_the_turtle.right(90)
# for i in range(4):
#     dashed_line()
#     dashed_line()
#     dashed_line()
#     dashed_line()
#     dashed_line()
#     dashed_line()
#     timmy_the_turtle_movement()
##########################

####Draw a Triange, Square, Pentagon, Hexagon, Heptagon, Octagon, Nonagun, Decagon####
# def line():
#     timmy_the_turtle.forward(100)
# def triangle_angle():
#     timmy_the_turtle.right(120)
# def square_angle():
#     timmy_the_turtle.right(90)
# def pentagon_angle():
#     timmy_the_turtle.right(72)
# def hexagon_angle():
#     timmy_the_turtle.right(60)
# def heptagon_angle():
#     i = 360/7
#     timmy_the_turtle.right(i)
# def octagon_angle():
#     timmy_the_turtle.right(45)
# def nonagon_angle():
#     timmy_the_turtle.right(40)
# def decagon_angle():
#     timmy_the_turtle.right(36)

# def triangle():
#     for _ in range(3):
#         line()
#         triangle_angle()

# def square():
#     for _ in range(4):
#         line()
#         square_angle()

# def pentagon():
#     for _ in range(5):
#         line()
#         pentagon_angle()

# def hexagon():
#     for _ in range(6):
#         line()
#         hexagon_angle()

# def heptagon():
#     for _ in range(7):
#         line()
#         heptagon_angle()

# def octagon():
#     for _ in range(8):
#         line()
#         octagon_angle()
    
# def nonagon():
#     for _ in range(9):
#         line()
#         nonagon_angle()

# def decagon():
#     for _ in range(10):
#         line()
#         decagon_angle()

# triangle()
# square()
# pentagon()
# hexagon()
# heptagon()
# octagon()
# nonagon()
# decagon()

##########################

####Draw a random walk####
# angle = [0, 90, 180, 270, 360]
# color = ["black", "yellow", "green", "red", "blue", "violet", "indigo", "violet", "pink", "orange", "grey", "brown"]

# for i in range(500):
#     choice = random.choice(angle)
#     color_choice = random.choice(color)
#     timmy_the_turtle.pensize(10)
#     timmy_the_turtle.speed(50)
#     timmy_the_turtle.forward(50)
#     timmy_the_turtle.left(choice)
#     timmy_the_turtle.color(color_choice)
##########################

#####Make a spirograph####

# color = ["black", "yellow", "green", "red", "blue", "violet", "indigo", "violet", "pink", "orange", "grey", "brown"]

# for i in range(100):
#     color_choice = random.choice(color)
#     timmy_the_turtle.speed(50)
#     timmy_the_turtle.circle(50)
#     timmy_the_turtle.right(5)
#     timmy_the_turtle.color(color_choice)
###########################




screen = Screen()
screen.exitonclick()