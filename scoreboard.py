from turtle import Turtle

FONT = ("Courier", 24, "normal")
SCOREBOARD_POSITION = (-200, 265)


class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(SCOREBOARD_POSITION)

    def update_score(self):
        self.clear()
        self.write(arg=f"Level :{self.score}", align="center", font=FONT)

    def level_passed(self):
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)
