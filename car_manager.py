from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
PADDING = 50
SHAPE = "square"


class CarManager(Turtle):

    def __init__(self, max_height, min_height, max_width):
        super().__init__(shape=SHAPE)
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.y_cord = random.randrange(min_height+PADDING, max_height-PADDING)
        self.x_cord = max_width
        self.x_move = MOVE_INCREMENT
        self.goto(x=self.x_cord, y=self.y_cord)

    def increase_speed(self):
        self.x_move += 5

    def move(self):
        new_x_cord = self.xcor() - self.x_move
        self.goto(y=self.y_cord, x=new_x_cord)
