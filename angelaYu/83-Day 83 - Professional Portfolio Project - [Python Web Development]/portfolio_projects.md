# Portfolio Projects — Python Web Development (Day 83)

No solution code exists for these. That's the assignment: research it, design it, build it,
deploy it, and be able to explain every decision in an interview.

Pick **two or three**, finish them properly (deployed, documented, polished), and put them
at the top of your GitHub profile.

---

## What every portfolio project needs

- [ ] A live URL (deployed — a screenshot is not a project)
- [ ] A GitHub repo with a real README: what it is, screenshots, how to run it locally
- [ ] Your own code, not a tutorial copy — even the styling should be yours
- [ ] At least one feature that *wasn't* in any course lesson
- [ ] A short "what I'd do next" section — shows you think beyond the first version

---

## Project briefs

### 1. Blog with users (upgrade your Day 68 app)
* Bcrypt passwords, register/login/logout
* Only the author can edit or delete their post (`current_user.id == post.author_id`)
* Rich text or markdown posts, comments, admin flag for privileged users
* **Stretch:** image uploads, tags, search

### 2. To-do list / habit tracker
* Multi-user, with a database
* Add, complete, delete, filter (today / week / all)
* **Stretch:** streaks, statistics per habit, email reminder (Days 32 + 37 skills)

### 3. Personal portfolio site
* "My projects" cards linking to everything you've built
* Contact form that actually sends email (use env vars, never hard-code credentials)
* Custom domain if you can
* **Stretch:** a `/now` page, dark mode

### 4. Data-entry / scraping service
* Scrape a public site on a schedule (Days 45–53 tooling)
* Store results in PostgreSQL, show them in a Flask dashboard
* **Stretch:** charts with Matplotlib/Plotly, alert emails when something changes

### 5. REST API + client
* Build the API (Day 66 style) with full documentation
* Write a small client that consumes it (CLI or web page)
* **Stretch:** token authentication, rate limiting, tests

### 6. Something from an industry you care about
* A recipe manager, a gym scheduler, a league table, a reading tracker
* The best portfolio projects solve a problem *you* have — you'll finish them

---

## README template

```markdown
# Project name

One sentence: what it does and who it's for.

![screenshot](screenshot.png)

## Live demo
https://your-app.example.com  (test account: demo / demo1234)

## Features
- …
- …

## Built with
Python · Flask · SQLAlchemy · PostgreSQL · Bootstrap · deployed on …

## Running locally
```bash
git clone …
pip install -r requirements.txt
export FLASK_KEY=…
python main.py
```

## What I learned
Two or three honest sentences about the hard parts and how you solved them.
```

---

## Before you call it finished

| Check | Why |
|-------|-----|
| Works on mobile | recruiters open links on phones |
| No secrets in the repo | `.gitignore`, env vars, rotated keys |
| Handles bad input gracefully | 404/400 pages instead of tracebacks |
| Database persists across restarts | PostgreSQL, not a local file |
| Someone else has used it | watch a friend try it — you'll learn a lot |
