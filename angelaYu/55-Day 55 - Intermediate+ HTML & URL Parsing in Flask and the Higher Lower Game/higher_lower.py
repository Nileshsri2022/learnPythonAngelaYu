"""
Day 55 Project: Guess the Number ("Higher or Lower") web game.

Routes:
    /           -> prompt to guess a number between 0 and 9
    /<guess>    -> "Too low", "Too high", or "You found me!" + a GIF

Plus the decorator challenge from the lesson: @make_bold, @make_emphasis and
@make_underline are stacked on the /bye route instead of typing tags by hand.

Run:  python higher_lower.py   (then open http://127.0.0.1:5000)
"""

import random

from flask import Flask

app = Flask(__name__)

ANSWER = random.randint(0, 9)


# ----------------------------------------------------------------------
# Decorator challenge: style a returned string without writing tags inline
# ----------------------------------------------------------------------
def make_bold(function):
    def wrapper(*args, **kwargs):
        return "<b>" + function(*args, **kwargs) + "</b>"
    return wrapper


def make_emphasis(function):
    def wrapper(*args, **kwargs):
        return "<em>" + function(*args, **kwargs) + "</em>"
    return wrapper


def make_underline(function):
    def wrapper(*args, **kwargs):
        return "<u>" + function(*args, **kwargs) + "</u>"
    return wrapper


# ----------------------------------------------------------------------
# Routes
# ----------------------------------------------------------------------
@app.route("/")
def home():
    return ('<h1 style="text-align: center; color: #7b1fa2">'
            "Guess a number between 0 and 9</h1>"
            '<p style="text-align: center">'
            "Add it to the address bar, e.g. <code>/3</code></p>")


@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def say_bye():
    return "Bye!"


@app.route("/username/<name>")
def greet(name):
    return f"Hello {name}!"


@app.route("/<int:guess>")
def guess_number(guess):
    if guess < ANSWER:
        return '<h1 style="color: #1976d2">Too low, try again!</h1>'
    if guess > ANSWER:
        return '<h1 style="color: #d32f2f">Too high, try again!</h1>'
    return ('<h1 style="color: #388e3c">You found me!</h1>'
            '<img src="https://media.giphy.com/media/4xpB3eE00FfBm/giphy.gif" '
            'width="300" alt="celebration">')


if __name__ == "__main__":
    app.run(debug=True)
