import time
from paddle import Paddle
from brickmap import BrickMap
from ball import Ball
from scoreboard import ScoreBoard
from turtle import Screen

screen = Screen()
screen.setup(width=728, height=550)
screen.title("Python Turtle Breakout Game")
screen.bgcolor("black")
screen.tracer(0)

game_is_on = True
bricks_layout = BrickMap()
p = Paddle()
ball = Ball()
scoreboard = ScoreBoard()


def start_game():
    global game_is_on, bricks_layout, p, ball, scoreboard
    while game_is_on:
        time.sleep(0.005)
        ball.move()

        # Defect if ball hits a wall or paddle
        if ball.xcor() > 350 or ball.xcor() < -350:
            ball.bounce_x()
        if ball.ycor() > 255:
            ball.bounce_y()

        for unit in p.paddle:
            if ball.distance(unit) < 14:
                ball.bounce_y()

        # Detect if ball falls
        if ball.ycor() < -231:
            scoreboard.decrease_lives()
            ball.reset_position()
            p.reset()

        # Detect if ball hits a brick
        for brick in bricks_layout.bricks:
            for brick_unit in brick.units:
                if ball.distance(brick_unit) < 14:
                    bricks_layout.delete_brick(bricks_layout.bricks.index(brick))
                    scoreboard.add_points()
                    ball.bounce_y()
                    if len(bricks_layout.bricks) % 10 == 0:
                        ball.increase_speed()
                    break

        if len(bricks_layout.bricks) == 0:
            scoreboard.print_completed()
            game_is_on = False

        if scoreboard.lives == 0:
            scoreboard.print_over()
            game_is_on = False

        screen.update()


def restart():
    global game_is_on, bricks_layout, scoreboard, ball
    if not game_is_on:
        game_is_on = True
        scoreboard.reset_score()
        bricks_layout.reset_layout()
        ball.reset_speed()
        ball.reset_position()
        start_game()


screen.listen()
screen.onkey(p.move_left, "Left")
screen.onkey(p.move_right, "Right")
screen.onkey(restart, "space")

start_game()

screen.exitonclick()
