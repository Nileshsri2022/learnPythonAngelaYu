Here is a structured breakdown of this lesson introducing version control and Git.

---

### 1. The Problem: "Save Point 1", "Save Point 2", "Final_final_v3"

You write code, it grows, and at some point you change something and break everything.
Without version control you have two options: keep dozens of copied folders, or despair.

**Version control** records *save points* — snapshots of your project you can go back to at
any time.

---

### 2. What Git Gives You

| Capability | Why it saves you |
|------------|------------------|
| Save points (commits) | return to any previous state |
| Diffs | compare today's mess with the last working version |
| Time travel | move backwards *and* forwards between versions |
| Branches | try something risky without touching working code |
| History | see what changed, when, and why |

Because code is interconnected (class A depends on class B), a small mistake can cascade.
Being able to roll back 20 minutes — or 20 commits — is what keeps you fast.

---

### 3. Git vs GitHub

| | What it is |
|--|-----------|
| **Git** | the version-control program that runs locally on your machine |
| **GitHub** | a website that hosts Git repositories, for sharing and collaborating |

Git works offline; GitHub is where the copies live so others (and future-you, on another
machine) can reach them.

---

### 4. The Vocabulary You'll Meet

* **Repository (repo)** — a project tracked by Git (a folder containing a hidden `.git`).
* **Working directory** — the files you're editing right now.
* **Staging area** — files selected for the next save point.
* **Commit** — a save point, with a message.
* **Remote** — a repo hosted elsewhere (GitHub).
* **Branch** — an independent line of development.

---

### 5. What's Coming

```
create a repo → make commits → push to GitHub → ignore files you shouldn't commit
→ clone someone else's repo → branch & merge → fork & pull request
```

---

### Summary Checklist

1. Version control = save points you can always return to.
2. Git is local; GitHub hosts remote copies.
3. Commits and branches let you experiment without fear.
4. Learn the vocabulary — every Git tutorial assumes it.
