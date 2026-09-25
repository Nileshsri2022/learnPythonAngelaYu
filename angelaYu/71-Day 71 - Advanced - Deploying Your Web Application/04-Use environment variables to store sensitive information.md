Here is a structured breakdown of this lesson on environment variables for sensitive information.

---

### 1. The Problem

Your app needs secrets: a Flask `SECRET_KEY`, an email password, API keys, a database URL.
Hard-coded values in `main.py` end up in the repository, where anyone can read them — and
Git history keeps them forever.

---

### 2. Environment Variables

Values that live in the **environment**, not in the code:

```python
import os

app.config["SECRET_KEY"] = os.environ.get("FLASK_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///posts.db")
```

* The code says *"get me `FLASK_KEY`"* — it doesn't say what the value is.
* Locally you supply them in `.env`; the host supplies them in its dashboard.

---

### 3. The `.env` File (local only)

```bash
FLASK_KEY=your-long-random-secret
DATABASE_URL=sqlite:///posts.db
MY_EMAIL=you@example.com
MY_EMAIL_PASSWORD=app-specific-password
```

Load it automatically with **python-dotenv**:

```python
from dotenv import load_dotenv
load_dotenv()            # reads .env into os.environ before anything else runs
```

> **⚠️ Warning:** `.env` must be in `.gitignore`. It's the single file most likely to leak
> a password into a public repository.

---

### 4. On the Hosting Platform

Each platform has a *Config Vars* / *Environment Variables* panel:

| Platform | Where |
|----------|-------|
| Heroku | Settings → Config Vars |
| Render | Environment → Environment Variables |
| Railway / Fly.io | Variables / Secrets |
| PythonAnywhere | Web → Environment variables |

Add the same keys with production values (different database URL, different secret key).
Nothing in the repository changes.

---

### 5. Good Practice

| Do | Don't |
|----|-------|
| Provide defaults for non-secrets: `os.environ.get("X", "fallback")` | Provide defaults for secrets |
| Use a long random `SECRET_KEY` (`python -c "import secrets; print(secrets.token_hex(32))"`) | Reuse your development key in production |
| Rotate a key immediately if it leaks | Email/commit/share secrets |
| Document required keys in `.env.example` (values blank) | Commit the real `.env` |

`.env.example` is how a teammate knows which variables to set:

```bash
FLASK_KEY=
DATABASE_URL=
```

---

### Summary Checklist

1. Secrets go in environment variables, never in source code.
2. `.env` + `python-dotenv` for local development; the host's dashboard in production.
3. `os.environ.get("KEY")` reads them; `.env` stays out of Git.
4. Ship `.env.example` so setup is reproducible; rotate anything that leaked.
