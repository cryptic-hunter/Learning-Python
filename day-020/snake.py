from turtle import Turtle

#Declaration of a constant#
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)] 
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
            # segment_1 = Turtle(shape="square")
            # segment_1.color("white")

            # segment_2 = Turtle(shape="square")
            # segment_2.color("white")
            # segment_2.goto(-20, 0)

            # segment_3 = Turtle(shape="square")
            # segment_3.color("white")
            # segment_3.goto(-40, 0)
            
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    
    def extend(self):
        #add a new segment to the snake
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

#####Inheritance Example#####
# class Fish(Animal):
#     def __init__(self):
#         super().__init__(self) # Super refers to the superclass
#initializing everything that the super class can do in the current class
#############################

# #####Inheritance Example Code#####
# class Animal:
#     def __init__(self):
#         self.num_eyes = 2
#     def breathe(self):
#         print("Inhale, Exhale")

# class Fish(Animal):
#     def __init__(self):
#         super().__init__()
#     def swim(self):
#         print("moving in water")
#     #when a class wants to inherit a method from super class
#     def breathe(self):
#         super().breathe()
#         print("Doing this underwater.")
# nemo = Fish()
# nemo.swim()
# nemo.breathe()
# ######EXAMPLE CODE END######