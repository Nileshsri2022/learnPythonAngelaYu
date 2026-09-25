"""
Day 68 Project: authentication with Flask.

A tiny site with registration, login, logout, flash messages and a /secrets
page that only logged-in users can reach. Passwords are salted and hashed with
Werkzeug (bcrypt/PBKDF2), and sessions are managed by Flask-Login.

Setup:
    pip install flask flask-sqlalchemy flask-login
    export FLASK_KEY="a-long-random-secret"      # Windows: set FLASK_KEY=...
Run:
    python main.py   ->  http://127.0.0.1:5000
"""

import os

from flask import Flask, flash, redirect, render_template, request, url_for
from flask_login import (LoginManager, UserMixin, current_user, login_required,
                         login_user, logout_user)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("FLASK_KEY", "dev-only-change-me")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"          # where @login_required sends guests


# ----------------------------------------------------------------------
# Model
# ----------------------------------------------------------------------
class User(UserMixin, db.Model):
    """UserMixin supplies the interface Flask-Login expects."""

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))     # a salted hash, never the password
    name = db.Column(db.String(1000))


@login_manager.user_loader
def load_user(user_id):
    """Session cookie -> user id -> User object, on every request."""
    return db.session.get(User, int(user_id))


# ----------------------------------------------------------------------
# Routes
# ----------------------------------------------------------------------
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        name = request.form.get("name")
        password = request.form.get("password")

        if db.session.execute(db.select(User).where(User.email == email)).scalar():
            flash("You've already signed up with that email, log in instead!", "error")
            return redirect(url_for("login"))

        if len(password) < 8:
            flash("Please use at least 8 characters.", "error")
            return redirect(url_for("register"))

        new_user = User(
            email=email,
            name=name,
            # salt + hash in one call; salt_length is configurable
            password=generate_password_hash(password, method="pbkdf2:sha256", salt_length=8),
        )
        db.session.add(new_user)
        db.session.commit()

        flash("Account created - please log in.", "success")
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = db.session.execute(
            db.select(User).where(User.email == email)
        ).scalar()

        if not user:
            flash("That email does not exist, please try again.", "error")
            return redirect(url_for("login"))

        if not check_password_hash(user.password, password):
            flash("Password incorrect, please try again.", "error")
            return redirect(url_for("login"))

        login_user(user)
        flash(f"Welcome back, {user.name}!", "success")
        return redirect(url_for("secrets"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    logout_user()
    flash("You've been logged out.", "success")
    return redirect(url_for("home"))


@app.route("/secrets")
@login_required                      # anonymous visitors are redirected to /login
def secrets():
    return render_template("secrets.html", name=current_user.name)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
