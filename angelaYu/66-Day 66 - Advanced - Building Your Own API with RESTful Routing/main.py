"""
Day 66 Project: a RESTful API for a database of cafes.

Endpoints (JSON):
    GET    /random                          one random cafe
    GET    /all                             every cafe
    GET    /search?location=London          cafes in a location
    POST   /add                             create a cafe (form fields)
    PATCH  /update-price/<cafe_id>?new_price=£4.20
    DELETE /report-closed/<cafe_id>?api_key=TopSecretAPIKey

Setup:  pip install flask flask-sqlalchemy
Run:    python main.py   ->  http://127.0.0.1:5000
Test:   Postman (or curl) for POST / PATCH / DELETE.
"""

import os
import random

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# SQLite database in the project folder; create it on first run.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

API_KEY = os.environ.get("CAFE_API_KEY", "TopSecretAPIKey")


class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self) -> dict:
        """A database row as a plain dictionary - ready for jsonify()."""
        return {column.name: getattr(self, column.name)
                for column in self.__table__.columns}


def all_cafes() -> list[Cafe]:
    return db.session.execute(db.select(Cafe).order_by(Cafe.name)).scalars().all()


# ----------------------------------------------------------------------
# HTML routes
# ----------------------------------------------------------------------
@app.route("/")
def home():
    return render_template("index.html", cafes=all_cafes())


# ----------------------------------------------------------------------
# API routes
# ----------------------------------------------------------------------
@app.route("/random")
def get_random_cafe():
    cafes = all_cafes()
    if not cafes:
        return jsonify(error={"Not Found": "No cafes in the database yet."}), 404
    return jsonify(cafe=random.choice(cafes).to_dict())


@app.route("/all")
def get_all_cafes():
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes()])


@app.route("/search")
def search_cafes():
    location = request.args.get("location")
    if not location:
        return jsonify(error={"Bad Request":
                              "Add a location, e.g. /search?location=London"}), 400

    cafes = db.session.execute(
        db.select(Cafe).where(Cafe.location.ilike(location))
    ).scalars().all()

    if cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in cafes])
    return jsonify(error={"Not Found":
                          "Sorry, we don't have a cafe at that location."}), 404


@app.route("/add", methods=["POST"])
def add_cafe():
    required = ["name", "map_url", "img_url", "location", "seats", "coffee_price"]
    missing = [field for field in required if not request.form.get(field)]
    if missing:
        return jsonify(error={"Bad Request":
                              f"Missing fields: {', '.join(missing)}"}), 400

    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        seats=request.form.get("seats"),
        has_toilet=bool(request.form.get("has_toilet")),
        has_wifi=bool(request.form.get("has_wifi")),
        has_sockets=bool(request.form.get("has_sockets")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        coffee_price=request.form.get("coffee_price"),
    )
    try:
        db.session.add(new_cafe)
        db.session.commit()
    except Exception:                                  # unique-name violation, etc.
        db.session.rollback()
        return jsonify(error={"Bad Request": "That cafe already exists."}), 400

    return jsonify(response={"success": "Successfully added the new cafe."}), 201


@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_coffee_price(cafe_id):
    cafe = db.session.get(Cafe, cafe_id)
    if cafe is None:
        return jsonify(error={"Not Found":
                              "Sorry, a cafe with that id was not found."}), 404

    new_price = request.args.get("new_price")
    if not new_price:
        return jsonify(error={"Bad Request": "Missing ?new_price=..."}), 400

    cafe.coffee_price = new_price          # PATCH: only this one field changes
    db.session.commit()
    return jsonify(success="Successfully updated the coffee price."), 200


@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    # authorisation first, so we never leak which ids exist
    if request.headers.get("api-key", request.args.get("api_key")) != API_KEY:
        return jsonify(error={"Forbidden": "Sorry, that's not the valid api key."}), 403

    cafe = db.session.get(Cafe, cafe_id)
    if cafe is None:
        return jsonify(error={"Not Found":
                              "Sorry, a cafe with that id was not found."}), 404

    db.session.delete(cafe)
    db.session.commit()
    return jsonify(success="Deleted the cafe."), 200


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
