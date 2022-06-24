from turtle import Turtle

PADDLE_COLOR = "azure3"
PADDLE_UNIT_STRETCH = 0.7
PADDLE_UNIT_SIZE = 14  # 20 *stretch_len
MOVE_DIST = PADDLE_UNIT_SIZE
INIT_X = PADDLE_UNIT_SIZE * 5 / 2 * -1  # Center - 1/2 unit size
INIT_Y = -210


class Paddle:

    def __init__(self):
        self.paddle = []
        x = INIT_X
        for i in range(6):
            unit = Turtle("square")
            unit.penup()
            unit.shapesize(stretch_len=PADDLE_UNIT_STRETCH, stretch_wid=PADDLE_UNIT_STRETCH)
            unit.color(PADDLE_COLOR)
            unit.goto(x, INIT_Y)
            self.paddle.append(unit)
            x += PADDLE_UNIT_SIZE
        self.paddle_left = self.paddle[0]
        self.paddle_right = self.paddle[5]

    def move_left(self):
        if self.paddle_left.xcor() > -350:
            for i in range(len(self.paddle)):
                self.paddle[i].backward(MOVE_DIST)

    def move_right(self):
        if self.paddle_right.xcor() < 343:
            for i in range(len(self.paddle)):
                self.paddle[i].forward(MOVE_DIST)

    def reset(self):
        x = INIT_X
        for i in range(len(self.paddle)):
            self.paddle[i].goto(x, INIT_Y)
            x += PADDLE_UNIT_SIZE
