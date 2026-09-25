Here is a structured breakdown of this lesson on GitHub and remote repositories.

---

### 1. Local vs Remote

Your commits so far live only on your machine. A **remote repository** (on GitHub) is a
copy on someone else's server — backup, collaboration and portfolio in one.

---

### 2. Create the Repository on GitHub

1. Sign up / sign in at **github.com**.
2. Click **+ → New repository**.
3. Name it (`Story`), add a description.
4. Choose visibility:
   * **Public** — anyone can read it (most repos; great for portfolios and learning from
     others)
   * **Private** — only you and invited collaborators
5. *Don't* initialise with a README if you already have local commits — an empty repo makes
   the push simpler.

---

### 3. Connect Local to Remote

GitHub shows the commands after creating the repo:

```bash
git remote add origin https://github.com/yourname/Story.git
git branch -M main
git push -u origin main
```

| Piece | Meaning |
|-------|---------|
| `origin` | the conventional name for "the remote I cloned from / will push to" |
| `-M main` | rename the local branch to `main` (GitHub's default) |
| `push` | upload your commits |
| `-u` | remember the pairing, so later `git push` alone works |

---

### 4. The Day-to-Day Commands

```bash
git push                     # send local commits to the remote
git pull                     # fetch remote commits and merge them into your copy
git remote -v                # which remotes are configured
git clone <url>             # the way *others* start working on it
```

Flow of a day:

```
pull → code → add → commit → push
```

> **Tip:** Pull before you push. If GitHub has commits you don't have, the push is
> rejected and you'll need to merge first.

---

### 5. Authentication

* HTTPS: username + a **personal access token** (or a stored credential helper).
* SSH: generate a key pair, add the public key to GitHub, then use the `git@github.com:…`
  URL.

Never paste tokens into shared code or commit them — that's what `.gitignore` is for
(next lesson).

---

### 6. Why Make It Public?

Reading other people's repositories — their structure, naming and commit messages — is one
of the fastest ways to learn. Publishing yours returns the favour, and gives recruiters
something to look at.

---

### Summary Checklist

1. GitHub hosts your repo; Git manages it locally.
2. `git remote add origin <url>` + `git push -u origin main` publishes everything.
3. `git push` uploads, `git pull` downloads, `git clone` copies a repo down.
4. Pull before pushing; authenticate with a token or SSH key, never a committed password.
