from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        # this below is used to write on our screen, using turtle library
        # self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        self.update_scoreboard()  # alternatively

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()  # this clears the previous score text/number in the scoreboard
        # self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        self.update_scoreboard()  # alternatively
