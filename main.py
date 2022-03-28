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
BG_COLOUR = "gainsboro"

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor(BG_COLOUR)
screen.title("Turtle crossing")
screen.tracer(0)
screen.listen()

player = Player()
cars = CarManager(max_height=MAX_HEIGHT,
                  min_height=MIN_HEIGHT,
                  max_width=MAX_WIDTH)

screen.onkeypress(fun=player.move, key="Up")

score = Scoreboard(max_height=MAX_HEIGHT, min_width=MIN_WIDTH)

game_is_on = True
current_level = player.level
while game_is_on:
    time.sleep(0.1)
    screen.update()

    for car in cars.cars:
        if car.distance(player) < 20:
            score.game_over()
            game_is_on = False

    if player.level > current_level:
        cars.increase_difficulty()
        score.level_up()
        current_level = player.level

    cars.add_car()
    cars.move()

screen.exitonclick()