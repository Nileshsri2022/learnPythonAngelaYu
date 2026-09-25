# Upgrade SQLite Database to PostgreSQL

---

### 1. Why SQLite Isn't Enough in Production

| | SQLite | PostgreSQL |
|--|--------|-----------|
| Storage | a file on disk | a real database server |
| Concurrency | one writer at a time | many concurrent users |
| Persistence | tied to the container's disk | managed, backed up, durable |
| Features | minimal | types, indexes, transactions, JSON |

On many platforms the local file system is **ephemeral** — every deploy or restart wipes
your SQLite file, taking every registered user with it. PostgreSQL is a service, so the
data outlives the code.

---

### 2. Provision the Database

In the hosting dashboard: add a PostgreSQL add-on/plugin (usually one click) and copy the
connection URL it provides:

```text
postgresql://user:password@host:5432/dbname
```

Store it as the `DATABASE_URL` environment variable.

---

### 3. Point the App at It

```python
import os

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "DATABASE_URL",                       # production, from the host
    "sqlite:///posts.db",                 # local development fallback
)
```

* Locally, no `DATABASE_URL` is set, so SQLite is used.
* In production, the platform's value wins — same code, different environment.

> **Note:** Some platforms (Heroku historically) hand out `postgres://` URLs, but
> SQLAlchemy expects `postgresql://`. Normalise it if your deploy fails to connect:

```python
uri = os.environ.get("DATABASE_URL", "sqlite:///posts.db")
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
app.config["SQLALCHEMY_DATABASE_URI"] = uri
```

---

### 4. Install the Driver

```bash
pip install psycopg2-binary
pip freeze > requirements.txt          # or add it by hand
```

`psycopg2` is the Python↔PostgreSQL adapter; `-binary` avoids needing build tools on the
host.

---

### 5. Create the Tables and Seed Data

```python
with app.app_context():
    db.create_all()
```

`db.create_all()` creates missing tables in whichever database you're connected to. For SQL
or existing data locally, migrate with `pg_dump` / `psql`, or write a small seed script —
but for a fresh deployment, creating the tables and registering a user through the UI is
enough.

> **⚠️ Warning:** Never point production at a database you're still experimenting with, and
> never commit the `DATABASE_URL` — it contains the database password.

---

### 6. Verify

* Register a user on the live site.
* Redeploy / restart the service.
* Log in again — the account still exists, so the data lives in PostgreSQL, not in the
  container.

---

### Summary Checklist

1. SQLite's file is lost on restarts and can't handle concurrent users.
2. Add the platform's PostgreSQL service and copy its connection URL.
3. Read `DATABASE_URL` from the environment, with SQLite as the local default.
4. Install `psycopg2-binary` and add it to `requirements.txt`.
5. `db.create_all()` builds the schema; a restart test proves persistence.
