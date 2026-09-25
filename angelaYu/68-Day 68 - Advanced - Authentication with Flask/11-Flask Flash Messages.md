# Flask Flash Messages

---

### 1. The Problem With `return "Password incorrect"`

Dumping an error string on a blank page loses the form, the styling and the user's place.
What you want is a message shown *on the page* — once — then forgotten.

That's exactly what `flash()` does: store a message in the session, display it on the next
rendered page, then discard it.

---

### 2. Sending a Message

```python
from flask import flash

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = db.session.execute(
            db.select(User).where(User.email == request.form.get("email"))
        ).scalar()

        if not user:
            flash("That email does not exist, please try again.", "error")
            return redirect(url_for("login"))

        if not check_password_hash(user.password, request.form.get("password")):
            flash("Password incorrect, please try again.", "error")
            return redirect(url_for("login"))

        login_user(user)
        flash("Logged in successfully!", "success")
        return redirect(url_for("secrets"))
```

* `flash(message, category)` — the category (`"error"`, `"success"`) lets the template style
  messages differently.
* Redirect after posting (POST → Redirect → GET). Without the redirect, a refresh
  re-submits the form.

---

### 3. Displaying Messages

```html
{% with messages = get_flashed_messages(with_categories=true) %}
    {% if messages %}
        {% for category, message in messages %}
            <div class="alert alert-{{ category }}">{{ message }}</div>
        {% endfor %}
    {% endif %}
{% endwith %}
```

* `get_flashed_messages()` returns (and clears) pending messages — each one shows exactly
  once.
* `with_categories=true` pairs each message with the category you passed to `flash()`.
* `{% with %} … {% endwith %}` assigns a value for use inside the block (Jinja's local
  variable).

---

### 4. Flashing Requires a Session

`flash()` stores messages in the session, so `app.secret_key` must be configured — the same
key Flask-Login uses to sign its cookie.

---

### 5. Good Places to Flash

| Event | Message |
|-------|---------|
| Failed login | "Password incorrect, please try again." |
| Successful login | "Welcome back, Angela!" |
| Registration | "Account created — please log in." |
| Logout | "You've been logged out." |
| Permission denied | "You need to be logged in to view that page." |

> **Tip:** Keep messages short and human. They're read in a fraction of a second next to
> the thing that went wrong.

---

### Summary Checklist

1. `flash(msg, category)` queues a one-time message in the session.
2. Display with `get_flashed_messages(with_categories=true)` in the template.
3. Redirect after a POST so refreshes don't resubmit.
4. Categories map neatly onto CSS classes for error/success styling.
