"""
Day 56 Project: Personal Name Card website served by Flask.

Project layout Flask expects:

    my-personal-site/
    ├── server.py            <- this file
    ├── templates/
    │   └── index.html       <- the name card page
    └── static/
        ├── styles.css       <- name card styling
        └── images/
            └── avatar.png   <- drop your own photo here

Run:  python server.py   then open http://127.0.0.1:5000
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    """Serve the name card template."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
