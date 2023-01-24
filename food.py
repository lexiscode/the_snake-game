# Reads: from the turtle module import Turtle class
from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)  # makes it 10 by 10 circle, initial from 20 by 20
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        # remember the size of the screen is 600 by 600, in coordinate system is divided by 300 by 300 [ + ]
        # so we had to reduce the positions of foods so that the snake will not hit the wall, hence 280 by 280
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
