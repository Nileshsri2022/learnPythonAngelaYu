"""Day 18 code: the five turtle challenges + the Hirst dot painting."""

import random
import turtle

from turtle import Turtle

turtle.colormode(255)

timmy = Turtle()
timmy.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


# ---- Challenge 1: square ----
def draw_square():
    for _ in range(4):
        timmy.forward(100)
        timmy.right(90)


# ---- Challenge 2: dashed line ----
def draw_dashed_line():
    for _ in range(15):
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()


# ---- Challenge 3: shapes from triangle to decagon ----
def draw_shapes():
    colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
               "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
    for shape_side_n in range(3, 11):
        timmy.color(random.choice(colours))
        angle = 360 / shape_side_n
        for _ in range(shape_side_n):
            timmy.forward(100)
            timmy.right(angle)


# ---- Challenge 4: random walk ----
def random_walk():
    timmy.pensize(15)
    directions = [0, 90, 180, 270]
    for _ in range(200):
        timmy.color(random_color())
        timmy.forward(30)
        timmy.setheading(random.choice(directions))


# ---- Challenge 5: spirograph ----
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)


# ---- Project: Hirst dot painting ----
COLOR_LIST = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135),
              (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185),
              (198, 91, 17), (46, 122, 86), (72, 43, 35), (145, 178, 148),
              (13, 99, 71), (233, 175, 164), (160, 142, 158), (54, 45, 50),
              (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89)]


def draw_hirst_painting(dots_per_row=10, rows=10):
    timmy.penup()
    timmy.hideturtle()
    timmy.setheading(225)
    timmy.forward(300)
    timmy.setheading(0)

    for dot_count in range(1, dots_per_row * rows + 1):
        timmy.dot(20, random.choice(COLOR_LIST))
        timmy.forward(50)
        if dot_count % dots_per_row == 0:
            timmy.setheading(270)
            timmy.forward(50)
            timmy.setheading(180)
            timmy.forward(50 * dots_per_row)
            timmy.setheading(0)


# Uncomment one at a time to run:
# draw_square()
# draw_dashed_line()
# draw_shapes()
# random_walk()
# draw_spirograph(5)
# draw_hirst_painting()

screen = turtle.Screen()
screen.exitonclick()
