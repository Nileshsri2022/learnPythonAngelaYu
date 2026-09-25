"""
Day 54: first web server with Flask + the decorator concepts behind @app.route.

Run `python3 main.py`, then visit http://127.0.0.1:5000/ (and /bye) in a
browser. Ctrl+C stops the server.
"""

import time

from flask import Flask

# ------------------------------------------------------------ decorators 101
def delay_decorator(function):
    """Returns a version of `function` that waits 2 seconds before running."""

    def wrapper_function():
        time.sleep(2)
        function()

    return wrapper_function


def speed_calc_decorator(function):
    """Prints how long `function` took."""

    def wrapper():
        start = time.time()
        function()
        end = time.time()
        print(f"{function.__name__} took {end - start:.6f}s")

    return wrapper


@speed_calc_decorator
def fast_function():
    for _ in range(10_000_000):
        pass


@speed_calc_decorator
def slow_function():
    for _ in range(100_000_000):
        pass


# ------------------------------------------------------------- the web server
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


@delay_decorator
@app.route("/bye")
def bye():
    return "Bye!"


# `__name__` == "__main__" only when this file is run directly (not imported).
if __name__ == "__main__":
    fast_function()
    slow_function()
    app.run(debug=True)
