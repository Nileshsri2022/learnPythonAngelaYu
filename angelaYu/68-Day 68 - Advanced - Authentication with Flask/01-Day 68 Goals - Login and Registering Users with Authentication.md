Here is a structured breakdown of this lesson on the goals for Day 68.

---

### 1. Why Authentication At All?

Users generate data — posts, likes, messages, recipes. To attach that data to a specific
person you need an **account**: a username, a password, and an ID in the database. Then the
same credentials let them come back and see only *their* things.

Two jobs authentication does:

| Job | Example |
|-----|---------|
| Identify users | "these messages belong to you" |
| Restrict access by status | Netflix/Spotify: paying subscribers only |

---

### 2. The Project

A deliberately tiny site with two buttons and one prize:

```
/            Home  →  [Register]  [Login]
/register    Pick username + password
/login       Enter them again
/secrets     🔒 Only visible to logged-in users
```

Simple layout, because the interesting part is **security**, not CSS.

---

### 3. The Security Ladder

Over the next lectures you climb through increasingly serious password storage:

| Level | Storage | Verdict |
|-------|---------|---------|
| 0 | plain text | never |
| 1 | encrypted (reversible) | better, but the key can be stolen |
| 2 | **hashed** (one-way) | decent |
| 3 | **hashed + salted** | good |
| 4 | bcrypt with salt rounds | industry standard |

---

### 4. Tools You'll Use

* **Werkzeug** — Flask's own hashing utilities (`generate_password_hash`,
  `check_password_hash`).
* **Flask-Login** — session management: `login_user`, `logout_user`, `@login_required`,
  `current_user`.
* **Flash messages** — one-time notifications ("You've been logged out").

---

### Summary Checklist

1. Authentication = accounts, so user data belongs to someone.
2. It also gates premium/private areas of a site.
3. Password storage escalates: plain text → encryption → hash → hash + salt → bcrypt.
4. Today's stack: Werkzeug + Flask-Login + flash messages.
