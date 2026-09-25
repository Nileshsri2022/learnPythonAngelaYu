Here is a structured breakdown of this lesson on authenticating users with Flask-Login.

---

### 1. What Flask-Login Gives You

Sessions — the browser carries a cookie, and Flask-Login maps it back to a user object on
every request.

| Tool | Purpose |
|------|---------|
| `login_manager` | initialises the extension |
| `login_user(user)` | start a session |
| `logout_user()` | end it |
| `@login_required` | protect a route |
| `current_user` | the logged-in user, available everywhere |

---

### 2. Wiring It Up

```python
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    """Given a session's user id, return the matching User object."""
    return db.session.get(User, int(user_id))
```

* The `User` model must inherit `UserMixin` (Day 68's starter project).
* `user_loader` is called on **every** request: session cookie → user id → `User` object.
* `login_manager.login_view = "login"` sends anonymous users to your login page.

---

### 3. Log In / Log Out

```python
@app.route("/login", methods=["GET", "POST"])
def login():
    ...
    if user and check_password_hash(user.password, password):
        login_user(user)
        return redirect(url_for("secrets"))


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))
```

The session cookie is signed with `app.secret_key` — set it from an environment variable:

```python
app.config["SECRET_KEY"] = os.environ.get("FLASK_KEY", "dev-key-change-me")
```

> **⚠️ Warning:** Anyone who knows your `SECRET_KEY` can forge session cookies. Never ship
> the development default; never commit the real one.

---

### 4. Protecting Routes

```python
@app.route("/secrets")
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name)
```

* Anonymous visitors are redirected to the login view instead of seeing the page.
* Order matters: `@app.route` outermost, `@login_required` beneath it.

---

### 5. The Whole Flow

```
register → hash the password → save the user
login    → check_password_hash → login_user() → session cookie
request  → user_loader() → current_user is the real User object
/secrets → @login_required → only for logged-in users
logout   → logout_user() → cookie cleared
```

---

### Summary Checklist

1. Initialise `LoginManager`, provide a `user_loader`.
2. `UserMixin` on the model supplies the required interface.
3. `login_user()` / `logout_user()` start and end sessions.
4. `@login_required` guards routes; `current_user` is available inside them.
5. The session cookie is signed with `SECRET_KEY` — keep it secret and out of git.
