Here is a structured breakdown of this lesson on registering new users.

---

### 1. The Route

```python
from flask import Flask, render_template, request, redirect, url_for

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # form values, read by the `name` attributes of the inputs
        email = request.form.get("email")
        name = request.form.get("name")
        password = request.form.get("password")

        # 1. does this user already exist?
        existing = db.session.execute(
            db.select(User).where(User.email == email)
        ).scalar()
        if existing:
            return "You've already signed up with that email. Log in instead."

        # 2. create and store the new user (hashing comes later today)
        new_user = User(email=email, name=name, password=password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("login"))

    return render_template("register.html")
```

* One route, two methods: `GET` serves the form, `POST` handles the submission —
  the classic pattern.
* `url_for("login")` sends the fresh user to the login page (Day 57's URL building).

---

### 2. The Form

```html
<form method="post" action="{{ url_for('register') }}">
    <input type="email"    name="email"    placeholder="Email" required>
    <input type="text"     name="name"     placeholder="Name" required>
    <input type="password" name="password" placeholder="Password" required>
    <button type="submit">Sign me up</button>
</form>
```

The `action` posts back to the same route; the field `name`s are the keys
`request.form.get()` reads.

---

### 3. Rules Worth Enforcing

| Rule | Why |
|------|-----|
| Email unique | one account per address |
| All fields required (`required` + server-side check) | users can bypass HTML validation |
| Password length ≥ 8 | short passwords are brute-forced instantly |
| Never echo the password back | obvious, but people do it |

---

### 4. What's Wrong With This Version?

The password goes into the database **as typed**. That's the "level 0" security from the
goals lecture — fine to *demonstrate* the flow, unacceptable to ship. The next lectures fix
it: hash it, then salt it, then use Werkzeug's bcrypt-based helper.

---

### Summary Checklist

1. `methods=["GET", "POST"]` — GET shows the form, POST processes it.
2. Read fields with `request.form.get("field-name")`.
3. Check for an existing email before inserting.
4. `db.session.add()` + `commit()`, then redirect to login.
5. Storing the raw password is the bug the rest of the day fixes.
