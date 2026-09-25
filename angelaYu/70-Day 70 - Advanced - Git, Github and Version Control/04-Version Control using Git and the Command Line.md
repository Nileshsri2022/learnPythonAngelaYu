Here is a structured breakdown of this lesson on version control with Git on the command line.

---

### 1. Build the Practice Project

```bash
cd ~/Desktop
mkdir Story && cd Story
touch chapter1.txt
open chapter1.txt        # Windows: notepad chapter1.txt
```

Write a line, save, close. One file, no version control yet.

---

### 2. Initialise a Repository

```bash
git init
```

Creates a hidden `.git` folder — the entire history lives there.

```bash
ls -a            # -a shows hidden files: .git is there
```

* **Working directory** — `Story/`, the files as you see them.
* **Staging area** — the intermediate holding spot for files you want in the next commit.
* A file that isn't staged is **untracked**.

---

### 3. Stage and Commit

```bash
git status                 # untracked files shown in red
git add chapter1.txt       # move it to the staging area
git status                 # now green: "Changes to be committed"
git commit -m "Add chapter 1"
```

* `git add <file>` selects exactly what goes into the snapshot — useful for committing one
  logical change at a time.
* `git add .` stages everything in the current folder.
* `-m "message"` records *why*: write messages in the imperative ("Add chapter 1", not
  "added stuff").

---

### 4. See the History

```bash
git log                    # full commits: hash, author, date, message
git log --oneline          # one line per commit — the practical view
```

Each commit has a unique **hash** (`a1b2c3d…`) — Git's name for that save point.

---

### 5. Compare and Roll Back

```bash
git diff                   # working directory vs staged version
git diff HEAD              # working directory vs the last commit
git checkout <hash> -- file.txt   # restore one file from an old commit
git revert <hash>          # make a new commit that undoes an old one
git reset --hard <hash>    # discard everything after <hash> (destructive!)
```

> **⚠️ Warning:** `git reset --hard` throws away uncommitted work with no confirmation.
> Prefer `git revert` when the commits are already pushed somewhere.

---

### 6. The Daily Loop

```
edit files → git status → git add <files> → git commit -m "why"
```

Small, frequent commits with clear messages are the whole discipline.

---

### Summary Checklist

1. `git init` creates the repository (the `.git` folder).
2. `git status` shows what's untracked (red) and staged (green).
3. `git add` stages; `git commit -m "message"` creates the save point.
4. `git log --oneline` is the readable history; `git diff` shows pending changes.
5. You can restore any file from any earlier commit — that's the point of it all.
