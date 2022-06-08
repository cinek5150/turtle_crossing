import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")
screen.onkey(player.right, "Right")
screen.onkey(player.left, "Left")

game_is_on = True
cars.spawn_start()

while game_is_on:
    time.sleep(0.01)
    cars.move()

    for car in cars.all_cars:
        if player.distance(car) < 20:
            player.refresh()
        if player.ycor() > 280:
            scoreboard.increase_score()
            player.refresh()
            cars.increase_speed()
        if car.xcor() < -330:
            cars.all_cars.remove(car)
            cars.spawn_next()
    screen.update()
