# Download the Starting Project

---

### 1. Get the Starter Project

The course provides a small Flask site so you can concentrate on authentication:

```text
flask-auth/
├── main.py             # Flask app + SQLite database
├── templates/
│   ├── index.html      # home page with Register / Login buttons
│   ├── register.html
│   ├── login.html
│   └── secrets.html    # the protected page
└── static/
    └── css/styles.css
```

---

### 2. Install the Dependencies

```bash
pip install flask flask-sqlalchemy flask-login werkzeug
# or
pip install -r requirements.txt
```

| Package | Purpose |
|---------|---------|
| Flask | the app |
| Flask-SQLAlchemy | the `User` table |
| Flask-Login | sessions: `login_user`, `@login_required`, `current_user` |
| Werkzeug | password hashing (`generate_password_hash`) |

---

### 3. The User Model

```python
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))
    name = db.Column(db.String(1000))
```

* `UserMixin` supplies the methods Flask-Login expects (`is_authenticated`, `get_id`, …) —
  inheritance from Day 21 doing real work.
* `password` will store a **hash**, never the real password. The 200-character column is
  deliberate: hashes are long.

---

### 4. Run It

```bash
python main.py
# http://127.0.0.1:5000
```

The pages render; the buttons lead nowhere useful yet — that's the work ahead.

---

### Summary Checklist

1. Starter project = Flask + SQLAlchemy + four templates.
2. Install Flask, Flask-SQLAlchemy, Flask-Login and Werkzeug.
3. `User(UserMixin, db.Model)` is the account table.
4. The password column will hold a hash — make it wide (200 chars).
