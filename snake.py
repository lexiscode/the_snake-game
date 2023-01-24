from turtle import Turtle

# coordinate positions of three turtles in a single line
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]  # this variable is used in the main.py

    def create_snake(self):
        # this produces/initializes and sets positions for the three squared turtles
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("green")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        # add a new segment to the snake
        # we are getting hold of the last segment in our list here using that -1 counting
        self.add_segment(self.segments[-1].position())

    def move(self):
        # below makes the tails (other turtles) follow where the head (first turtle) is going
        for seg_num in range(len(self.segments) - 1, 0, -1):  # range(2, 0, -1)
            # taking their x and y coordinates below
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        # this will ensure it cant go DOWN while it's going UP, even if the Down key is pressed
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        # this will ensure it cant go UP while it's going DOWN, even if the Up key is pressed
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        # this will ensure it cant go RIGHT while it's going LEFT, even if the Right key is pressed
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)
            # or self.segments[0].left

    def right(self):
        # this will ensure it cant go LEFT while it's going RIGHT, even if the Left key is pressed
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
            # or self.segments[0].right
