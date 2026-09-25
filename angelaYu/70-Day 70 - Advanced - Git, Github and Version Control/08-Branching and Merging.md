Here is a structured breakdown of this lesson on branching and merging.

---

### 1. Why Branches?

A branch is an independent line of development. Use one when you:

* build a risky feature you might throw away,
* fix a bug while `main` stays stable,
* work with others without overwriting each other's code.

`main` stays the working version; branches are where experiments happen safely.

---

### 2. The Commands

```bash
git branch                      # list branches (* marks the current one)
git checkout -b feature-x       # create AND switch to a new branch
git checkout main               # switch back
git branch -d feature-x         # delete a merged branch
```

> **Note:** `git switch -c feature-x` is the modern equivalent of `checkout -b`; both work.

---

### 3. Working on the Branch

```bash
git checkout -b dog-branch
# edit files
git add .
git commit -m "Teach the dog to fetch"
git push -u origin dog-branch      # publish the branch (needed for PRs)
```

Commits made here don't touch `main` until you merge.

---

### 4. Merging

```bash
git checkout main               # the branch you're merging INTO
git merge dog-branch            # bring the other branch's commits in
```

Two possible outcomes:

| Result | Meaning |
|--------|---------|
| **Fast-forward / clean merge** | no conflicting edits — done |
| **Merge conflict** | both branches changed the same lines |

Conflict markers look like:

```
<<<<<<< HEAD
price = 3
=======
price = 4
>>>>>>> dog-branch
```

Edit the file to keep what you want, delete the markers, then:

```bash
git add .
git commit -m "Resolve merge conflict in pricing"
```

---

### 5. Good Habits

* One branch per feature or fix — small, focused changes merge easily.
* Merge often; long-lived branches drift and conflict.
* Keep `main` deployable at all times.
* Delete the branch after merging.

```bash
git checkout main
git merge dog-branch
git push
git branch -d dog-branch
```

---

### Summary Checklist

1. Branches let you experiment without risking `main`.
2. `git checkout -b name` creates and switches; `git branch` lists.
3. Merge by checking out the target branch and running `git merge <other>`.
4. Conflicts are edited by hand, then `git add` + `commit`.
5. Push branches when you want a pull request; delete them once merged.
