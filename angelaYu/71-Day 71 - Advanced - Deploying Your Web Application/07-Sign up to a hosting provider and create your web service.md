Here is a structured breakdown of this lesson on signing up to a hosting provider.

---

### 1. What a Hosting Provider Gives You

A computer that is always on, connected to the internet, running your app — plus HTTPS, a
public URL, and a way to configure secrets and a database. You already built the app; the
platform supplies the machine.

Well-known options: Heroku, Render, Railway, Fly.io, PythonAnywhere, and any VPS where you
configure things yourself.

---

### 2. Create the Web Service

Typical flow (Render is the modern, free-tier-friendly analogue of the course's Heroku):

1. Sign up with your GitHub account.
2. **New → Web Service**.
3. Connect the repository you just pushed.
4. Configure:
   * **Build command**: `pip install -r requirements.txt`
   * **Start command**: `gunicorn main:app` (or let the `Procfile` supply it)
   * **Environment / runtime**: Python 3.x
5. Add the **environment variables** (`FLASK_KEY`, `DATABASE_URL`, email credentials…) —
   never in the repo.
6. Deploy.

---

### 3. Watch the Logs

The build log tells you exactly what happened:

| Symptom | Usual cause |
|---------|-------------|
| `ModuleNotFoundError: No module named 'gunicorn'` | missing from `requirements.txt` |
| `Error: Couldn't find a Flask application` | start command doesn't match `module:app` |
| App crashes immediately | missing environment variable |
| `Address already in use` | hard-coded port instead of using `$PORT` |
| 500 on every page | database not initialised / `SECRET_KEY` missing |

**Read the traceback from the bottom up** — the last line names the exception, the lines
above show where.

---

### 4. Configure the Database

Add the provider's PostgreSQL add-on, then copy the `DATABASE_URL` it gives you into your
environment variables. Your code reads it (next lesson), so no code change is needed beyond
that.

---

### 5. Test the Live Site

* Open the URL on your phone — the mobile experience is part of the check.
* Register a user, post something, restart the app: is the data still there? (It should be
  in PostgreSQL, not in an ephemeral file system.)
* Watch the logs while you click — every error you can recreate is easier to fix.

---

### 6. Free Tiers and Sleep

Many hosts hibernate free services after inactivity: the first request after a nap takes a
few seconds to wake. That's normal, not a bug — but worth knowing before you demo it to
someone.

---

### Summary Checklist

1. Connect the GitHub repo to a new web service.
2. Build command installs requirements; start command runs gunicorn.
3. Environment variables replace every local secret; `$PORT` comes from the platform.
4. Read build/runtime logs bottom-up to debug deployment failures.
5. Test the live site like a user, mobile included — and mind free-tier sleep.
