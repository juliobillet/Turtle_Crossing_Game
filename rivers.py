from turtle import Turtle


class Rivers(Turtle):

    def __init__(self, new_river_position):
        super(Rivers, self).__init__()
        self.penup()
        self.color("dodger blue")
        self.shape("square")
        self.resizemode("user")
        self.shapesize(stretch_wid=5, stretch_len=40)
        self.goto(new_river_position)
