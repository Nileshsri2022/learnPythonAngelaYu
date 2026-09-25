# Downloading Files

---

### 1. Why Download Instead of Type?

The blog/auth project needs a database, a user model, and half a dozen templates that have
nothing to do with today's lesson. Downloading them keeps the focus on **authentication**.

---

### 2. What You Should Have

```text
flask-auth/
├── main.py
├── instance/
│   └── users.db          # SQLite database (created on first run)
├── templates/
│   ├── index.html
│   ├── register.html
│   ├── login.html
│   └── secrets.html
└── static/css/styles.css
```

If `users.db` doesn't exist, the first run creates it:

```python
with app.app_context():
    db.create_all()
```

---

### 3. Check the Moving Parts Before Writing Code

1. `python main.py` starts with no errors.
2. `/` renders with Register/Login buttons.
3. `/register` and `/login` render their forms.
4. The `User` table exists in `instance/users.db` (open it with any SQLite browser, or
   `sqlite3 instance/users.db ".schema"`).

> **Tip:** SQLite stores the file, not the data, so deleting `instance/users.db` resets
> the app — handy while testing registration and login repeatedly.

---

### 4. Keeping Secrets Out of the Repo

Three files should never be committed:

```gitignore
instance/
*.db
.env
```

Passwords and API keys belong in environment variables (`.env` + `python-dotenv`), not in
`main.py`.

---

### 5. Be Careful With Community Files

Files downloaded from forums or shared drives can contain anything. Prefer the official
course resources; if you must use someone else's zip, read `main.py` before running it —
Python has no "are you sure?" prompt.

---

### Summary Checklist

1. Download the starter to focus on auth, not boilerplate.
2. First run creates the SQLite database via `db.create_all()`.
3. Verify all pages render and the `users` table exists.
4. Ignore the database and secret files in git; read third-party code before running it.
