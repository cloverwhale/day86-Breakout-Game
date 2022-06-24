from turtle import Turtle

BRICK_COLOR = "AntiqueWhite2"
BRICK_LENGTH = 4
BRICK_UNIT_STRETCH = 0.7
BRICK_UNIT_SIZE = 20 * BRICK_UNIT_STRETCH


class Brick:

    def __init__(self, x, y):
        self.units = []
        brick_unit_position = x
        for i in range(BRICK_LENGTH):
            unit = Turtle("square")
            unit.penup()
            unit.shapesize(stretch_len=BRICK_UNIT_STRETCH, stretch_wid=BRICK_UNIT_STRETCH)
            unit.color(BRICK_COLOR)
            unit.goto(brick_unit_position, y)
            self.units.append(unit)
            brick_unit_position += BRICK_UNIT_SIZE

    def hide(self):
        for unit in self.units:
            unit.hideturtle()
            unit.clear()
