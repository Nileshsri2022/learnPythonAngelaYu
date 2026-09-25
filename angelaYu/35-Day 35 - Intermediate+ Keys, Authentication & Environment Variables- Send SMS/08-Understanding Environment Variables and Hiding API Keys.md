# Understanding Environment Variables and Hiding API Keys

The app works — but your API key and Twilio token are sitting in `main.py` as plain
strings. One `git push` and they belong to the internet. Time to hide them.

---

### 1. What Environment Variables Are

Your computer (and every server) keeps a list of **key = value** pairs that programs
can read. See them with:

```bash
env        # macOS / Linux
set        # Windows
```

Each line is a variable name, an `=` and a string value. PythonAnywhere has its own
slightly different list — the environment belongs to *where the code runs*.

---

### 2. Why You Want Them

| Reason | Example |
|--------|---------|
| **Convenience** | Change a value (an email list, a URL) without touching deployed code |
| **Security** | Keys live *outside* the code base, so they can't leak with it |

The danger is not PythonAnywhere — it is **GitHub/Bitbucket**: code hosting is
basically public Dropbox, and anyone reading your file can steal a key that is
committed in it. Free-tier keys feel harmless; the moment you upgrade to paid, a
stolen key costs you money.

---

### 3. Using Them

```bash
export OWM_API_KEY=8a6f...            # no spaces around "="
export AUTH_TOKEN=1b2c...
env | grep OWM                        # confirm they are set
```

```python
import os

API_KEY = os.environ.get("OWM_API_KEY")        # instead of "8a6f..."
auth_token = os.environ.get("AUTH_TOKEN")      # instead of "1b2c..."
```

The code is unchanged otherwise — `python3 main.py` still queues the SMS.

---

### 4. Scheduled Tasks Need Them Too

A cron task starts a **fresh environment**, so export the variables in the command
itself, chained with semicolons:

```bash
export OWM_API_KEY=8a6f...; export AUTH_TOKEN=1b2c...; python3 main.py
```

Now the task works even though `main.py` contains no secrets.

---

### 5. Finish and Explore

* Replace the test coordinates (Łódź/Bern) with your own latitude and longitude.
* Rain alert complete: *API keys + SMS + environment variables*.
* Next APIs to play with: Open Movie Database, Spotify — the skills are the same:
  read the docs, find the endpoint, pass parameters, authenticate.

---

### Summary Checklist

1. Environment variables are `KEY=value` strings of the environment your code runs in.
2. They give you **configurability** and, more importantly, **secrecy**.
3. `export NAME=value` (no spaces) then `os.environ.get("NAME")` in Python.
4. Never commit keys: a public repo is enough for someone to steal them.
5. For scheduled tasks, export the variables in the task command itself.
