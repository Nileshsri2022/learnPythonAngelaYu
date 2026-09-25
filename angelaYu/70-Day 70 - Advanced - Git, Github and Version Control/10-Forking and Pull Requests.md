# Forking and Pull Requests

---

### 1. The Open-Source Problem

You can clone anyone's public repo, but you can't push to it — you don't own it. To
contribute code you need a two-step dance: **fork**, then **pull request**.

---

### 2. Fork = Your Own Copy on GitHub

Click **Fork** in the top-right of a repository. GitHub creates `yourname/repo` — a full
copy on your account, which you *do* have push access to.

```text
github.com/original-owner/project   ← upstream (read-only to you)
github.com/yourname/project         ← your fork (yours to change)
```

---

### 3. The Contribution Workflow

```bash
# 1. clone YOUR fork
git clone https://github.com/yourname/project.git
cd project

# 2. make a branch for the change
git checkout -b fix-typo-in-readme

# 3. change, stage, commit
git add README.md
git commit -m "Fix typo in installation section"

# 4. push the branch to YOUR fork
git push -u origin fix-typo-in-readme
```

GitHub then shows a **Compare & pull request** button.

---

### 4. The Pull Request

A pull request (PR) asks the maintainer to pull your branch into their project.

Write it well:

| Section | Content |
|---------|---------|
| Title | what the change does, imperatively |
| Description | why it's needed, what you changed, how you tested it |
| Scope | one logical change per PR — not five unrelated fixes |
| Links | the issue it closes (`Closes #42`) |

Reviewers comment, request changes, and eventually approve. Once merged, your commits are
part of the project — and the contribution stays on your GitHub profile forever.

---

### 5. Keeping Your Fork Fresh

Your fork drifts as the original moves on. Sync it before starting new work:

```bash
git remote add upstream https://github.com/original-owner/project.git
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

Or use GitHub's **Sync fork** button.

---

### 6. Rules of Thumb

* Change as little as possible per PR — small PRs get reviewed, giant ones don't.
* Follow the project's contributing guide and code style.
* Don't include unrelated formatting or renames.
* Be patient and polite in review; maintainers are volunteers.

---

### Summary Checklist

1. Fork = your own server-side copy you can push to.
2. Branch → commit → push to your fork → open a PR against the original repo.
3. One logical change per pull request, with a clear description.
4. Keep the fork in sync via `upstream` (or the Sync fork button).
5. This workflow is exactly what teams use internally, too.
