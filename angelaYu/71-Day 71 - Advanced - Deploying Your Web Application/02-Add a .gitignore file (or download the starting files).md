Here is a structured breakdown of this lesson on adding a `.gitignore` file.

---

### 1. Before Anything Is Committed

Everything you commit is permanent history — including secrets if you get it wrong. Set up
`.gitignore` **first**, then commit.

If you're using the course's starting project, it may already include one; check before
writing your own.

---

### 2. A Deployment-Ready `.gitignore`

```gitignore
# Secrets — never commit these
.env
secrets.txt

# Python
__pycache__/
*.py[cod]
.venv/
venv/
*.egg-info/

# Local database + instance folder
instance/
*.sqlite
*.sqlite3
*.db

# macOS / Windows junk
.DS_Store
Thumbs.db

# Editors
.idea/
.vscode/
```

Note the entries that matter most on deployment day: `.env` and the local database. Both
exist only on your machine; the server gets its own.

---

### 3. Verify

```bash
git status              # .env / instance/ should not appear
git check-ignore -v .env
```

---

### 4. If You Already Committed Something Sensitive

```bash
git rm --cached .env
git commit -m "Stop tracking .env"
```

Then **rotate the exposed credential** — the old commit still contains it, and anyone who
clones the repo can read the history.

---

### 5. Download the Starting Files Instead?

The course offers a prepared project. If you take that route, still confirm:

* `.gitignore` excludes `.env`, `instance/`, `__pycache__/`,
* no passwords appear anywhere in `main.py`,
* `requirements.txt` lists every import the app uses.

---

### Summary Checklist

1. `.gitignore` before the first commit — history is forever.
2. Exclude `.env`, the local database, caches, virtualenvs and OS files.
3. Verify with `git status` and `git check-ignore -v`.
4. Already committed a secret? `git rm --cached`, commit, and rotate the credential.
