Here is a structured breakdown of this lesson on hashing and salting with Werkzeug.

---

### 1. Werkzeug Is Already Installed

Flask is built on Werkzeug, so `werkzeug.security` is available with no extra dependency:

```python
from werkzeug.security import generate_password_hash, check_password_hash
```

---

### 2. Generating the Hash at Registration

```python
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        name = request.form.get("name")

        if db.session.execute(db.select(User).where(User.email == email)).scalar():
            return "You've already signed up with that email. Log in instead."

        # salt + hash happen inside this one call
        hashed_password = generate_password_hash(
            request.form.get("password"),
            method="pbkdf2:sha256",     # default in modern Werkzeug; bcrypt also supported
            salt_length=8,
        )

        new_user = User(email=email, name=name, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("login"))

    return render_template("register.html")
```

The stored value looks like this — algorithm, salt and digest packed into one string:

```
pbkdf2:sha256:600000$Z8jK1pQ2$3f0a9c4b…
```

* `method` picks the algorithm (Werkzeug's default is salted PBKDF2-SHA256; `scrypt` and
  `bcrypt` are also available).
* `salt_length` sets how many random characters the salt gets.
* The salt is *inside* the stored string, so you never manage it yourself.

---

### 3. Checking at Login

```python
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = db.session.execute(
            db.select(User).where(User.email == email)
        ).scalar()

        if not user:
            return "That email does not exist, please try again."
        if not check_password_hash(user.password, password):
            return "Password incorrect, please try again."

        login_user(user)                    # Flask-Login: start the session
        return redirect(url_for("secrets"))

    return render_template("login.html")
```

`check_password_hash(stored, typed)` re-derives the hash from the typed password using the
salt embedded in the stored string, then compares — you never decrypt anything.

---

### 4. Rules

| Do | Don't |
|----|-------|
| Use `generate_password_hash` / `check_password_hash` | write your own salt/hash logic |
| Widen the DB column (200 chars) | assume hashes are short |
| Re-hash on password change | store a hash of a hash "for safety" |
| Keep Werkzeug updated | pin an ancient version |

> **Note:** The same 200-character column now holds a variable-length digest that changes
> with algorithm and rounds — another reason real applications use a generous column.

---

### Summary Checklist

1. `generate_password_hash(password, method=…, salt_length=8)` at registration.
2. `check_password_hash(stored_hash, typed_password)` at login.
3. Salt and algorithm are stored inside the hash string; you manage neither.
4. Werkzeug ships with Flask, uses proven algorithms and sane defaults.
