"""
Day 54: decorators, the mechanic behind Flask's @app.route.

Run:  python decorator_demo.py
"""

import time
from functools import wraps


# ----------------------------------------------------------------------
# 1. The decorator itself: a function that wraps another function.
# ----------------------------------------------------------------------
def delay_decorator(function):
    @wraps(function)                  # keep the original name/docstring
    def wrapper_function(*args, **kwargs):
        time.sleep(2)                 # extra behaviour BEFORE the call
        result = function(*args, **kwargs)
        return result                 # pass the original result through
    return wrapper_function           # return the function, not a call


@delay_decorator
def say_hello():
    print("hello")


def say_greeting():
    print("greeting")


# the long way — identical to putting @delay_decorator above the def
say_greeting = delay_decorator(say_greeting)


# ----------------------------------------------------------------------
# 2. Functions are first-class objects: pass one in as an argument.
# ----------------------------------------------------------------------
def add(n1, n2):
    return n1 + n2


def multiply(n1, n2):
    return n1 * n2


def calculate(calc_function, n1, n2):
    """Higher-order function: takes a function, calls it with two numbers."""
    return calc_function(n1, n2)


if __name__ == "__main__":
    say_hello()                       # waits 2 s, then prints hello
    say_greeting()                    # waits 2 s too - it's decorated
    print(calculate(multiply, 2, 3))  # 6
    print(calculate(add, 2, 3))       # 5
