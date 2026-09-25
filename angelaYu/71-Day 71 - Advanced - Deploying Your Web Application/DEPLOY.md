# Deploying the Flask blog — checklist

Everything Day 71 covers, in the order it happens. Work top to bottom; each step assumes
the one above it worked.

---

## 1. Prepare the project

- [ ] `.gitignore` includes `.env`, `instance/`, `*.db`, `__pycache__/`, `.venv/`
- [ ] No passwords or API keys anywhere in the source code
- [ ] `requirements.txt` exists (`pip freeze > requirements.txt`) and includes
      `gunicorn` and `psycopg2-binary`
- [ ] `Procfile` contains `web: gunicorn main:app`
- [ ] `debug=True` is **not** active in production code

## 2. Version control

```bash
git init
git add .
git status            # double-check nothing secret is staged
git commit -m "Initial commit: Flask blog"
```

## 3. Environment variables

- [ ] `python-dotenv` installed; `load_dotenv()` at the top of `main.py`
- [ ] `app.config["SECRET_KEY"] = os.environ.get("FLASK_KEY")`
- [ ] `app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///posts.db")`
- [ ] `.env.example` committed; `.env` ignored

## 4. WSGI server

```bash
pip install gunicorn
gunicorn main:app        # test locally: http://127.0.0.1:8000
```

- [ ] Local gunicorn run serves the site correctly

## 5. Push to GitHub

```bash
git remote add origin https://github.com/you/my-blog.git
git branch -M main
git push -u origin main
```

- [ ] On GitHub: no `.env`, no `.db`, `requirements.txt` and `Procfile` present

## 6. Hosting provider

- [ ] New Web Service connected to the repo
- [ ] Build command: `pip install -r requirements.txt`
- [ ] Start command: `gunicorn main:app`
- [ ] Environment variables added: `FLASK_KEY`, `DATABASE_URL`, email credentials
- [ ] First deploy succeeds (read the build log if not)
- [ ] Skip/limit free-tier sleep by visiting the URL before a demo

## 7. PostgreSQL

- [ ] PostgreSQL add-on created; `DATABASE_URL` copied into environment variables
- [ ] `postgres://` → `postgresql://` fix applied if the platform uses the old scheme
- [ ] `db.create_all()` runs on startup (or a one-off release command)
- [ ] Register a user on the live site → restart the service → log in again ✅

## 8. Ship it

- [ ] Open the URL on your phone
- [ ] Register, post, log out, log back in
- [ ] Share the link with someone who will try to break it
- [ ] Tag the release: `git tag v1.0 && git push --tags`

---

## Quick troubleshooting

| Error | Fix |
|-------|-----|
| `ModuleNotFoundError: gunicorn` | add it to `requirements.txt` |
| `Couldn't find a Flask application` | start command must be `module:app` |
| `Address already in use` | don't hard-code the port; use the platform's `$PORT` |
| 500 on every page | missing `SECRET_KEY` or `DATABASE_URL` |
| Data disappears after deploy | still on SQLite; move to PostgreSQL |
| `postgres://` connection error | replace the scheme with `postgresql://` |
