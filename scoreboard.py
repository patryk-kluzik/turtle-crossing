from turtle import Turtle

FONT = ("Courier", 18, "normal")

VERTICAL_PADDING = 40
HORIZONTAL_PADDING = 20


class Scoreboard(Turtle):

    def __init__(self, max_height, min_width):
        super().__init__()
        self.ht()
        self.penup()
        self.level = 1
        self.font_padding = (min_width+HORIZONTAL_PADDING, max_height-VERTICAL_PADDING)
        self.update_score()

    def update_score(self):
        self.clear()
        self.setposition(self.font_padding)
        self.write(arg=f"Level: {self.level}", font=FONT, align="left")

    def level_up(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.home()
        self.write(arg="GAME OVER", font=FONT, align="center")