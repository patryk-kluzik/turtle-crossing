from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
HEADING = 90


class Player(Turtle):

    def __init__(self):
        super().__init__("turtle")
        self.penup()
        self.color("green")
        self.goto(STARTING_POSITION)
        self.setheading(HEADING)

    def move(self):
        finished = self.check_if_level_complete()
        if finished:
            self.goto(STARTING_POSITION)
        else:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(y=new_y, x=self.xcor())

    def check_if_level_complete(self):
        return self.ycor() >= FINISH_LINE_Y
