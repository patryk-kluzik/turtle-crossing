import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

WIDTH = 600
HEIGHT = 600
MAX_HEIGHT = HEIGHT / 2
MIN_HEIGHT = - MAX_HEIGHT
MAX_WIDTH = WIDTH / 2
MIN_WIDTH = -MAX_WIDTH

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.tracer(0)

screen.listen()

player = Player()
car = CarManager(max_height=MAX_HEIGHT, min_height=MIN_HEIGHT, max_width=MAX_WIDTH)


screen.onkeypress(fun=player.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.move()
    print(car.fillcolor(), car.pencolor(), car.color)
    print(player.fillcolor(), player.pencolor(), player.color())

