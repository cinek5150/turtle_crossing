from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
         super(Player, self).__init__()
         self.penup()
         self.speed("fastest")
         self.color("white")
         self.shape("turtle")
         self.goto(STARTING_POSITION)
         self.setheading(90)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def down(self):
        self.back(MOVE_DISTANCE)

    def right(self):
        x_cor = self.xcor()
        y_cor = self.ycor()
        self.goto(x_cor+MOVE_DISTANCE, y_cor)

    def left(self):
        x_cor = self.xcor()
        y_cor = self.ycor()
        self.goto(x_cor-MOVE_DISTANCE, y_cor)

    def refresh(self):
        self.goto(STARTING_POSITION)