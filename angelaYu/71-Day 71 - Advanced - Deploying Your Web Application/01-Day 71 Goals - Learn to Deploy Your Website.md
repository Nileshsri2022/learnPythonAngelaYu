Here is a structured breakdown of this lesson on the goals for Day 71.

---

### 1. Today Your Website Goes Live

Everything so far has run on `127.0.0.1` — your machine only. Today the Flask blog is
published to the internet with a shareable URL anyone can visit, including from a phone.

---

### 2. The Tools

| Tool | Job |
|------|-----|
| **Git + GitHub** | version control and the source of truth the host deploys from |
| **Gunicorn** | a real WSGI server to run Flask in production |
| **A hosting provider** | a computer that's always on, running your app |
| **PostgreSQL** | a production database to replace SQLite |

---

### 3. The Deployment Path

```
1. .gitignore            keep secrets and local junk out of the repo
2. git init / commit     put the project under version control
3. environment variables read secrets from config, not source code
4. gunicorn              serve the app with a production-grade server
5. push to GitHub        the host pulls the code from there
6. hosting provider      create a web service, wire it to the repo
7. PostgreSQL            swap the development database for a real one
```

---

### 4. What Changes When You Go Live

| Development | Production |
|-------------|------------|
| `flask run` dev server | gunicorn (WSGI server) |
| SQLite file | PostgreSQL (managed database) |
| secrets in code | secrets in environment variables |
| localhost only | public URL, HTTPS, real users |
| `debug=True` | **must** be off |

> **⚠️ Warning:** Deploying with `debug=True` exposes the interactive debugger and your
> code's internals to the entire internet. Turn it off before you push.

---

### 5. Outcomes

* A live URL you can send to anyone.
* A repeatable deploy pipeline: commit → push → the platform rebuilds.
* The vocabulary to follow any deployment guide (Procfile, dyno, environment config).

---

### Summary Checklist

1. Today: development project → live website.
2. Git/GitHub + gunicorn + host + PostgreSQL.
3. Production differences: real server, real database, env-var secrets, debug off.
4. The seven-step path above is the checklist for the whole day.
