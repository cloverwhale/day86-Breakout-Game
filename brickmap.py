from brick import Brick

BRICK_ROWS = 5
BRICK_COLUMNS = 10
INIT_X = -342
INIT_Y = 220


class BrickMap:

    def __init__(self):
        self.bricks = []
        y = INIT_Y
        for i in range(BRICK_ROWS):
            x = INIT_X
            for j in range(BRICK_COLUMNS):
                brick = Brick(x, y)
                x = x + 70
                self.bricks.append(brick)
            y = y - 28

    def delete_brick(self, brick_index):
        self.bricks[brick_index].hide()
        self.bricks.remove(self.bricks[brick_index])

    def reset_layout(self):
        for brick in self.bricks:
            brick.hide()
        self.bricks.clear()
        self.__init__()
