Here is a structured breakdown of this lesson on downloading the starting project.

---

### 1. The Starting Files

The course ships a starter project containing:

```
cafe-api/
├── main.py            # Flask app + routes to fill in
├── templates/
│   ├── index.html     # the cafe list page (server-rendered)
│   └── add.html       # a form for adding cafes
├── static/
│   ├── css/styles.css
│   └── images/…
├── cafes.db           # SQLite database with the cafe records
└── requirements.txt
```

---

### 2. Set Up

```bash
pip install flask flask-sqlalchemy
# or: pip install -r requirements.txt
python main.py
```

Visit `http://127.0.0.1:5000` — the home page lists the cafes straight from the database.

---

### 3. The Database Model

```python
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

    def to_dict(self):
        """Return the row as a dictionary — ready to jsonify."""
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
```

* SQLAlchemy turns each row into a `Cafe` **object** (classes from Day 16–17 doing real
  work).
* `to_dict()` is the bridge between a database row and a JSON response.

---

### 4. What's Missing (Your Job)

The starter has the model, the database and the HTML routes. You'll add the **API routes**:

* `GET /random`
* `GET /all`
* `GET /search?location=…`
* `POST /add`
* `PATCH /update-price/<cafe_id>`
* `DELETE /report-closed/<cafe_id>`

---

### Summary Checklist

1. Starter project = Flask + SQLAlchemy + SQLite + HTML pages.
2. `db.Model` subclass describes the cafe table column by column.
3. `to_dict()` makes any row JSON-serialisable.
4. Today's work: add the six API endpoints to `main.py`.
