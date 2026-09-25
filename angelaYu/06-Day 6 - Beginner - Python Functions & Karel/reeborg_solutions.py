"""
Reeborg's World (Karel-style robot) solutions for Day 6.

These run at https://reeborg.ca/reeborg.html — the robot commands (move,
turn_left, at_goal, wall_in_front, ...) are provided by that environment,
so this file is documentation of the exact code to paste into Reeborg's editor.
"""


def turn_right():
    turn_left()
    turn_left()
    turn_left()


# ---- Hurdle 1: fixed six hurdles, solved with a for loop ----
def hurdle_1():
    def jump():
        move()
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        turn_left()

    for step in range(6):
        jump()


# ---- Hurdle 3: random number/position of hurdles -> while loop ----
def hurdle_3():
    def jump():
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()

    while not at_goal():
        if wall_in_front():
            jump()
        else:
            move()


# ---- Hurdle 4: random hurdle heights as well ----
def hurdle_4():
    def jump():
        turn_left()
        while wall_on_right():      # climb while wall blocks the right
            move()
        turn_right()
        move()
        turn_right()
        while front_is_clear():     # descend while front is open
            move()
        turn_left()

    while not at_goal():
        if wall_in_front():
            jump()
        else:
            move()


# ---- Final project: escape any maze with the right-wall algorithm ----
def escape_the_maze():
    while not at_goal():
        if right_is_clear():
            turn_right()
            move()
        elif front_is_clear():
            move()
        else:
            turn_left()
