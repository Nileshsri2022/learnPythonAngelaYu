"""Day 22 project: Pong — the famous arcade game.

Requires paddle.py, ball.py and scoreboard.py from this folder.
"""

import time

from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles.
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340:
        ball.bounce_x()
    if ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    # Detect when paddle misses.
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
