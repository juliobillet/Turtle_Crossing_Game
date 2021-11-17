from turtle import Screen
from player import Player
from trunk_manager import TrunkManager
from scoreboard import Scoreboard
from rivers import Rivers
import time

# CONSTANT VARIABLES.
RIVER_POSITIONS = ((0, -200), (0, -60), (0, 80), (0, 220))
# use Y from rivers to create trunks that appears inside the rivers perimeter.

# GLOBAL VARIABLES.
rivers = {}
game_over = False
move_speed = 0.1

# CREATING THE SCREEN FROM THE TURTLE MODULE SCREEN OBJECT.
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game 🐢")
screen.bgcolor("tan")
screen.tracer(0)

# CREATING THE MAIN OBJECTS OF THE GAME: RIVERS, TRUNKS, SCOREBOARD AND THE PLAYER.
for position in RIVER_POSITIONS:
    rivers["river_" + str(RIVER_POSITIONS.index(position) + 1)] = Rivers(position)
trunks = TrunkManager()
scoreboard = Scoreboard()
player = Player()

# LISTEN FUNCTIONS TO LISTEN FOR THE PLAYER'S COMMANDS ON THE KEYBOARDS.
screen.listen()
screen.onkeypress(player.go_up, "Up")
screen.onkeypress(player.go_down, "Down")

# DEBUG TEST TO SEE HOW THE RIVERS ARE BEING CREATED
# for river in rivers:
#    print(rivers[river].pos())
# print(rivers)

# MAIN LOOP OF THE GAME, ITS CORE WHILE LOOP.
while not game_over:
    screen.update()
    scoreboard.update_score()
    trunks.move_trunks()
    trunks.reset_trunks()

    # DETECT COLLISION OF THE PLAYER WITH THE TRUNKS. IF SO: GAME OVER.
    for trunk in trunks.trunks:
        if trunk.ycor() - 20 < player.ycor() < trunk.ycor() + 20 and \
                trunk.xcor() - 30 < player.xcor() < trunk.xcor() + 30:
            game_over = True
            scoreboard.game_over()

    # DETECT IF PLAYER IS PAST THE FINISH LINE. IF SO: RESET PLAYER, INCREASE LEVEL AND SPEED UP THE GAME/TRUNKS.
    if player.is_past_finish_line():
        scoreboard.level_passed()
        player.reset_player()
        move_speed -= 0.03

    time.sleep(move_speed)

# EXIT ON CLICK IF NECESSARY.
screen.exitonclick()
