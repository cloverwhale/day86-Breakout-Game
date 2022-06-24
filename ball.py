from turtle import Turtle

INIT_POSITION = (0, -196)
BALL_COLOR = "coral1"
INIT_SPEED = 2


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.7)  # 14 pixel
        self.penup()
        self.color(BALL_COLOR)
        self.goto(INIT_POSITION)
        self.move_x = INIT_SPEED
        self.move_y = INIT_SPEED

    def move(self):
        self.goto(self.xcor() + self.move_x, self.ycor() + self.move_y)

    def bounce_x(self):
        self.move_x *= -1

    def bounce_y(self):
        self.move_y *= -1

    def bounce_back(self):
        self.move_x *= -1
        self.move_y *= -1

    def increase_speed(self):
        self.move_x *= 1.2
        self.move_y *= 1.2

    def reset_position(self):
        self.goto(INIT_POSITION)

    def reset_speed(self):
        self.move_x = INIT_SPEED
        self.move_y = INIT_SPEED
