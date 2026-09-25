"""
Day 55 Project: Higher or Lower — played through Flask URLs.

Run `python3 main.py`, open http://127.0.0.1:5000/ and guess the random
number by typing it in the URL: http://127.0.0.1:5000/5
The page answers too low (red) / too high (purple) / correct (green),
then picks a fresh number for the next round.
"""

import random

from flask import Flask

app = Flask(__name__)
random_number = random.randint(0, 9)


@app.route("/")
def guess_number():
    return ("<h1 style='text-align: center'>Guess a number between 0 and 9"
            "</h1>"
            "<p style='text-align: center'>Type your guess in the URL: "
            "<code>/5</code></p>")


@app.route("/<int:guess>")
def check_guess(guess):
    global random_number
    if guess < random_number:
        return "<h1 style='color: red; text-align: center'>Too low, " \
               "try again!</h1>"
    elif guess > random_number:
        return "<h1 style='color: purple; text-align: center'>Too high, " \
               "try again!</h1>"
    else:
        random_number = random.randint(0, 9)  # new round, new number
        return ("<h1 style='color: green; text-align: center'>You got it!"
                "</h1>"
                "<p style='text-align: center'>A new number has been picked."
                "</p>")


if __name__ == "__main__":
    app.run(debug=True)
