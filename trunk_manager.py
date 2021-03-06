from turtle import Turtle
import random

TRUNK_POSSIBLE_Y_POS = [-240, -239, -238, -237, -236, -235, -234, -233, -232, -231, -230, -229, -228, -227, -226, -225,
                        -224, -223, -222, -221, -220, -219, -218, -217, -216, -215, -214, -213, -212, -211, -210, -209,
                        -208, -207, -206, -205, -204, -203, -202, -201, -200, -199, -198, -197, -196, -195, -194, -193,
                        -192, -191, -190, -189, -188, -187, -186, -185, -184, -183, -182, -181, -180, -179, -178, -177,
                        -176, -175, -174, -173, -172, -171, -170, -169, -168, -167, -166, -165, -164, -163, -162, -161,
                        -160, -100, -99, -98, -97, -96, -95, -94, -93, -92, -91, -90, -89, -88, -87, -86, -85, -84, -83,
                        -82, -81, -80, -79, -78, -77, -76, -75, -74, -73, -72, -71, -70, -69, -68, -67, -66, -65, -64,
                        -63, -62, -61, -60, -59, -58, -57, -56, -55, -54, -53, -52, -51, -50, -49, -48, -47, -46, -45,
                        -44, -43, -42, -41, -40, -39, -38, -37, -36, -35, -34, -33, -32, -31, -30, -29, -28, -27, -26,
                        -25, -24, -23, -22, -21, -20, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55,
                        56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79,
                        80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102,
                        103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 180,
                        181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199,
                        200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218,
                        219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237,
                        238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256,
                        257, 258, 259, 260]
COLORS = ["saddle brown", "sienna", "peru", "brown"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5  # Not used in this format, because for me, using the time.sleep method makes the game more fluid.


class TrunkManager:

    def __init__(self):
        self.trunks = self.create_trunks()

    @staticmethod
    def create_trunks():
        all_trunks = []
        for i in range(35):
            new_turtle = Turtle()
            new_turtle.penup()
            new_turtle.shape("square")
            new_turtle.resizemode("user")
            new_turtle.shapesize(stretch_wid=1, stretch_len=3)
            new_turtle.color(random.choice(COLORS))
            new_turtle.goto(x=random.randrange(-360, 300, 30), y=random.choice(TRUNK_POSSIBLE_Y_POS))
            all_trunks.append(new_turtle)
        return all_trunks

    def move_trunks(self):
        for trunk in self.trunks:
            trunk.backward(STARTING_MOVE_DISTANCE)

    def reset_trunks(self):
        for trunk in self.trunks:
            if trunk.xcor() <= -360:
                trunk.goto(x=320, y=random.choice(TRUNK_POSSIBLE_Y_POS))
