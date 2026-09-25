"""
Day 56 Project: Name Card website served with Flask.

Run `python3 main.py` and open http://127.0.0.1:5000/ — Flask renders
templates/index.html and serves static/css/style.css.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
