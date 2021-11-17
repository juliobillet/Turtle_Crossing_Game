from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super(Player, self).__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(90)
        self.reset_player()

    def go_up(self):
        if self.ycor() < FINISH_LINE_Y:
            self.forward(MOVE_DISTANCE)

    def go_down(self):
        if self.ycor() > FINISH_LINE_Y * -1:
            self.backward(MOVE_DISTANCE)

    def reset_player(self):
        self.goto(STARTING_POSITION)

    def is_past_finish_line(self):
        return self.ycor() >= FINISH_LINE_Y
