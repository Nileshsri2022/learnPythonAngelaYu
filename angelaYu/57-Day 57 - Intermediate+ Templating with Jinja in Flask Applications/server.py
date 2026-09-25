"""
Day 57 Project: a Jinja-templated blog (Part 1).

Routes:
    /                 -> list of posts (title + subtitle + "Read")
    /post/<id>        -> one post in full
    /guess/<name>     -> API + Jinja challenge (agify.io + genderize.io)
    /blog/<number>    -> url_for() demo with a URL variable

Run:  python server.py   then open http://127.0.0.1:5000
"""

import datetime

import requests
from flask import Flask, abort, render_template

app = Flask(__name__)

# Replace with your own JSON bin from npoint.io (or the course's endpoint).
BLOG_URL = "https://api.npoint.io/YOUR_BIN_ID"

# Fallback data so the site works before you create a bin.
all_posts = [
    {
        "id": 1,
        "title": "The Life of Cactus",
        "subtitle": "Very interesting. Who knew?",
        "body": "Cacti are succulents that store water in their stems.",
    },
    {
        "id": 2,
        "title": "Top 15 Things to Do When You're Bored",
        "subtitle": "Boredom is the mother of invention.",
        "body": "Number one: learn Python. Number two: see number one.",
    },
    {
        "id": 3,
        "title": "Introduction to Intermittent Fasting",
        "subtitle": "Turns out skipping breakfast is a lifestyle.",
        "body": "Intermittent fasting is an eating pattern, not a diet.",
    },
]


def fetch_posts():
    """Use the API bin when it's configured; otherwise the local sample data."""
    if "YOUR_BIN_ID" in BLOG_URL:
        return all_posts
    response = requests.get(BLOG_URL, timeout=20)
    response.raise_for_status()
    return response.json()


@app.route("/")
def get_all_posts():
    year = datetime.date.today().year
    return render_template("index.html", posts=fetch_posts(), year=year)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for post in fetch_posts():
        if post["id"] == index:
            requested_post = post
    if requested_post is None:
        abort(404)
    return render_template("post.html", post=requested_post)


@app.route("/blog/<int:number>")
def get_blog(number):
    """url_for() demo: the number is baked into the URL from the template."""
    print(f"Blog page requested with number={number}")
    return render_template("blog.html", posts=fetch_posts(), number=number)


@app.route("/guess/<name>")
def guess(name):
    """Challenge: combine two APIs with Jinja templating."""
    gender_data = requests.get(
        "https://api.genderize.io", params={"name": name}, timeout=20
    ).json()
    age_data = requests.get(
        "https://api.agify.io", params={"name": name}, timeout=20
    ).json()

    gender = gender_data.get("gender") or "a mystery"
    age = age_data.get("age") or "an unknown number of"
    return render_template("guess.html", name=name, gender=gender, age=age)


if __name__ == "__main__":
    app.run(debug=True)
