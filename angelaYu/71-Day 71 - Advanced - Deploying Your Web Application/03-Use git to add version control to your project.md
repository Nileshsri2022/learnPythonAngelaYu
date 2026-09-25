# Use git to add version control to your project

---

### 1. Why Git Is Part of Deployment

Hosting platforms don't upload files from your laptop — they **clone a repository** and run
it. So step one of going live is getting the project into Git.

---

### 2. Initialise and Commit

```bash
cd your-blog-project
git init
git add .
git commit -m "Initial commit: Flask blog"
git log --oneline
```

If Git complains about your identity:

```bash
git config --global user.name  "Your Name"
git config --global user.email "you@example.com"
```

---

### 3. Check What You're About to Commit

```bash
git status                 # anything unexpected? especially secrets?
git ls-files               # the final list of tracked files
```

Confirm by eye that `.env`, `instance/`, the SQLite database and `__pycache__/` are
**absent**.

---

### 4. Add the Deployment Files

The host also needs to know how to install and run your app:

**`requirements.txt`**

```bash
pip freeze > requirements.txt
```

```text
Flask==3.0.3
Flask-Login==0.6.3
Flask-SQLAlchemy==3.1.1
gunicorn==22.0.0
psycopg2-binary==2.9.9
python-dotenv==1.0.1
```

Trim development-only packages you don't need in production.

**`Procfile`** (used by Heroku-style platforms)

```text
web: gunicorn main:app
```

---

### 5. Commit the Rest

```bash
git add requirements.txt Procfile
git commit -m "Add deployment configuration"
```

Meaningful commit messages now matter: deployment platforms show them, and future-you will
read them when something breaks at 2 a.m.

---

### 6. Habits That Pay Off Here

* Commit small and often; every commit is a rollback point if a deploy fails.
* Never commit the database — production has its own, and user data must not live in a repo.
* Tag releases if you like (`git tag v1.0`) — handy for "what exactly is live?".

---

### Summary Checklist

1. `git init` + first commit puts the project under version control.
2. `requirements.txt` (via `pip freeze`) and `Procfile` are deployment prerequisites.
3. Verify with `git status` / `git ls-files` that no secrets or databases are tracked.
4. The host deploys from the repo, so the repo must be complete and clean.
