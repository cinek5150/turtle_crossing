from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 2
MOVE_INCREMENT = 1
STARTING_Y_TOP = 250
STARTING_Y_BOTTOM = -250
STARTING_X_RIGHT = 330
STARTING_X_LEFT = -330
CARS_AT_START = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.moving_speed = STARTING_MOVE_DISTANCE

    def spawn(self, x_cor, y_cor):
        self.new_car = Turtle()
        self.new_car.penup()
        self.new_car.setheading(180)
        self.new_car.goto(x_cor, y_cor)
        self.new_car.shapesize(1, 2.5)
        self.new_car.shape("square")
        self.new_car.speed("fastest")
        self.new_car.color(random.choice(COLORS))
        self.all_cars.append(self.new_car)

    def spawn_start(self):
        for car in range(0, CARS_AT_START):
            self.spawn(random.randint(STARTING_X_LEFT, STARTING_X_RIGHT),
                       random.randint(STARTING_Y_BOTTOM, STARTING_Y_TOP))

    def spawn_next(self):
        self.spawn(STARTING_X_RIGHT, random.randint(STARTING_Y_BOTTOM, STARTING_Y_TOP))

    def move(self):
        for car in self.all_cars:
            current_y = car.ycor()
            current_x = car.xcor()
            car.goto(current_x - self.moving_speed, current_y)

    def increase_speed(self):
        self.moving_speed += MOVE_INCREMENT
