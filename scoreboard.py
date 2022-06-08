from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.clear()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 260)
        self.score = 0
        self.write(f"Your score is {self.score}", font=FONT, align="center")

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Your score is {self.score}", font=FONT, align="center")