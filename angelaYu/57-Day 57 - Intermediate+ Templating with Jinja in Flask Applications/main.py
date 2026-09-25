"""
Day 57 Capstone Part 1: Blog with Jinja templating.

Three pages (home/about/contact) sharing a header, posts rendered from a
list with a Jinja for loop, nav links built with url_for.

Run `python3 main.py` → http://127.0.0.1:5000/
Swap the POSTS list for a requests.get(npoint_url).json() call to feed it
from the internet (the course's version uses npoint.io).
"""

from flask import Flask, render_template

app = Flask(__name__)

POSTS = [
    {
        "id": 1,
        "title": "The Day I Automated My Job",
        "subtitle": "Beautiful Soup, Selenium and a lot of free time",
        "body": "It started with a data-entry task nobody wanted. "
                "It ended with a Python script doing it in 40 seconds.",
    },
    {
        "id": 2,
        "title": "APIs Are Just Vending Machines",
        "subtitle": "POST, GET and the occasional stuck Twix",
        "body": "Once you see request/response as snack-dispensing, "
                "every API doc becomes a menu.",
    },
    {
        "id": 3,
        "title": "Why Flask Loves Decorators",
        "subtitle": "A Route, a Function and the @ Between Them",
        "body": "app.route is just a decorator wrapping your function "
                "in request-handling superpowers.",
    },
]


@app.route("/")
def get_all_posts():
    return render_template("index.html", posts=POSTS)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
