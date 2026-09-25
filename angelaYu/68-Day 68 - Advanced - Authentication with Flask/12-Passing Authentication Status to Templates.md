Here is a structured breakdown of this lesson on passing authentication status to templates.

---

### 1. The Nav Bar Problem

The navigation should show *Login/Register* to visitors but *Secrets/Logout* to logged-in
users. The template needs to know whether someone is authenticated.

---

### 2. `current_user` Is Already in the Template

Flask-Login injects `current_user` into every rendered template — no need to pass it in
`render_template`:

```html
<nav>
    <a href="{{ url_for('home') }}">Home</a>

    {% if current_user.is_authenticated %}
        <a href="{{ url_for('secrets') }}">Secrets</a>
        <a href="{{ url_for('logout') }}">Log out</a>
        <span>Hi, {{ current_user.name }}!</span>
    {% else %}
        <a href="{{ url_for('register') }}">Register</a>
        <a href="{{ url_for('login') }}">Login</a>
    {% endif %}
</nav>
```

* `current_user.is_authenticated` — `True` for a real logged-in user, `False` for the
  anonymous placeholder.
* `current_user.name` reads the column straight off the `User` model.
* One template, two states — no duplicated nav markup.

---

### 3. Personalising Pages

```html
<h1>Hello, {{ current_user.name }}!</h1>
<p>These are your secrets…</p>
```

Or pass it explicitly, which is useful when the route also needs other data:

```python
@app.route("/secrets")
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name)
```

---

### 4. Auth-Aware Behaviour Beyond the Nav

| Use | Template code |
|-----|---------------|
| Show an edit button only to the author | `{% if current_user.id == post.author_id %}` |
| Admin-only link | `{% if current_user.email == ADMIN_EMAIL %}` |
| "Log in to comment" prompt | `{% if not current_user.is_authenticated %}` |

> **⚠️ Warning:** Hiding a link is **not** security. Always re-check permissions on the
> server side — a hidden URL can still be typed in manually.

---

### 5. The Complete Site

```
/         home   — nav reflects auth state
/register POST   — hash password, save user, redirect to login
/login    POST   — check_password_hash, login_user, flash, redirect
/logout          — logout_user, redirect
/secrets         — @login_required, greets current_user.name
```

You now have real authentication: accounts, secure password storage, sessions, protected
pages and a UI that knows who's looking at it.

---

### Summary Checklist

1. `current_user` is available in every template automatically.
2. `{% if current_user.is_authenticated %}` switches the nav between guest/logged-in views.
3. `current_user.name` personalises the page; pass it explicitly when convenient.
4. Never rely on hidden UI for security — enforce permissions server-side too.
