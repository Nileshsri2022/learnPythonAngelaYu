"""
Day 54 Project: your first Flask web server.

Run it with the PyCharm play button, or from the terminal:

    export FLASK_APP=hello.py     # macOS/Linux
    set FLASK_APP=hello.py        # Windows
    flask run

Then open http://127.0.0.1:5000 in the browser. Stop the server with Ctrl+C
(or PyCharm's Stop button when using the `python hello.py` route).

Install Flask first:  pip install Flask
"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    """The home route: web-address + '/'."""
    return "<h1>Hello, World!</h1>"


@app.route("/bye")
def say_bye():
    return "Bye!"


if __name__ == "__main__":
    # app.run() == `flask run`, but with the IDE's normal run/stop controls.
    app.run(debug=True)
