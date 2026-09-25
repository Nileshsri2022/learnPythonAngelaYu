"""Day 25 project: U.S. States Game.

Requires the course assets: blank_states_img.gif and 50_states.csv
in the same folder.
"""

import turtle

import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name? (type 'Exit' to stop)")

    if answer_state is None:
        break
    answer_state = answer_state.title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        pandas.DataFrame(missing_states).to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        writer.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        writer.write(answer_state)

screen.exitonclick()
