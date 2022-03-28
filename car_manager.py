from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
MAX_MOVE_INCREMENT = 40
PADDING = 50
SPAWN_RATE = 20
MAX_SPAWN_RATE = 50
SHAPE = "square"


class CarManager:

    def __init__(self, max_height, min_height, max_width):
        self.cars = []
        self.max_height = max_height
        self.min_height = min_height
        self.max_width = max_width
        self.x_move = MOVE_INCREMENT
        self.spawn_rate = SPAWN_RATE
        self.add_car()

    def increase_difficulty(self):
        if self.x_move < MAX_MOVE_INCREMENT:
            self.x_move += 1
        if self.spawn_rate < MAX_SPAWN_RATE:
            self.spawn_rate += 2

    def move(self):
        for car in self.cars:
            car.back(self.x_move)

    def add_car(self):
        rand_num = random.randint(1,100)
        if rand_num < self.spawn_rate:
            new_car = Turtle(SHAPE)
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            y_cord = random.randrange(self.min_height + PADDING, self.max_height - PADDING)
            x_cord = self.max_width
            new_car.goto(x=x_cord, y=y_cord)
            self.cars.append(new_car)
