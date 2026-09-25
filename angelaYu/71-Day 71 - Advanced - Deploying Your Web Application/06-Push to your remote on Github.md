Here is a structured breakdown of this lesson on pushing your project to GitHub.

---

### 1. Create the Remote Repository

On GitHub: **+ → New repository**

* Name it (`my-blog`),
* choose Public or Private,
* **don't** add a README or `.gitignore` — you already have local commits and an empty
  remote keeps the push simple.

---

### 2. Connect and Push

Copy the URL GitHub shows and run:

```bash
git remote add origin https://github.com/yourname/my-blog.git
git branch -M main
git push -u origin main
```

| Command | Effect |
|---------|--------|
| `remote add origin <url>` | names the remote `origin` |
| `branch -M main` | renames your branch to `main` (GitHub's default) |
| `push -u origin main` | uploads commits and remembers the pairing |

Refresh the GitHub page: your files, commits and history are there.

---

### 3. Check the Push Before You Deploy

On GitHub, click through the repository and verify:

* [ ] `.env`, `instance/`, `*.db` and `__pycache__/` are **not** present
* [ ] no passwords visible in `main.py`
* [ ] `requirements.txt` and `Procfile` are present at the root
* [ ] the README explains what the app is

> **Note:** A repository is the artefact the host deploys. If something isn't in the repo,
> it doesn't exist in production.

---

### 4. Authentication

HTTPS pushes ask for a username and a **personal access token** (not your password), or use
an SSH key. GitHub's *Settings → Developer settings → Personal access tokens* creates one;
store it in your credential helper, never in the repo.

---

### 5. The Ongoing Workflow

```bash
git add .
git commit -m "Fix login redirect bug"
git push
```

Most hosting platforms watch the branch and **redeploy automatically** on every push to
`main` — that's the deploy loop you now own: commit → push → live.

> **Tip:** Keep `main` deployable. Experiment on a branch, open a pull request, merge when
> it works (Day 70's workflow) — that's how you avoid breaking the live site.

---

### Summary Checklist

1. Create an empty GitHub repo, then `git remote add origin <url>`.
2. `git push -u origin main` uploads everything and links the branches.
3. Verify on GitHub that no secrets or local files were published.
4. From now on, pushes to `main` become deployments.
