# Optional Git Challenge

---

### 1. The Challenge

Practise the whole workflow end to end, by yourself, without following along:

1. Create a new folder and `git init` it.
2. Add a file, stage it, commit it.
3. Make a second commit with a *useful* message.
4. Create a branch, add a file there, commit, and merge it back into `main`.
5. Create a `.gitignore` that excludes at least one secret file and one OS file.
6. Push the repository to GitHub.
7. Clone it into a *different* folder and confirm the history arrived.

---

### 2. Suggested Solution

```bash
mkdir git-challenge && cd git-challenge
git init

echo "hello" > notes.txt
git add notes.txt
git commit -m "Add notes"

git checkout -b more-notes
echo "second line" >> notes.txt
git commit -am "Extend notes"
git checkout main
git merge more-notes

printf 'secrets.txt\n.DS_Store\n__pycache__/\n' > .gitignore
touch secrets.txt
git add .gitignore
git commit -m "Ignore secrets and OS files"

git remote add origin https://github.com/yourname/git-challenge.git
git push -u origin main

cd ..
git clone https://github.com/yourname/git-challenge.git clone-check
cd clone-check && git log --oneline     # both commits are there
```

Handy shortcut: `git commit -am "message"` stages and commits **tracked** modifications in
one step (it won't add brand-new files).

---

### 3. Check Yourself

| Question | Answer you should be able to give |
|----------|-----------------------------------|
| What's the difference between the working directory and the staging area? | working = files as edited; staging = what goes into the next commit |
| Why did `secrets.txt` stay out of the repo? | the `.gitignore` rule (verify with `git status`) |
| What does `-u` in `push -u` do? | links the local branch to its remote counterpart |
| How do you undo the last commit but keep the changes? | `git reset --soft HEAD~1` |
| How do you see one line per commit? | `git log --oneline` |

---

### 4. Stretch Goals

* Revert a commit with `git revert <hash>` and read the new commit it creates.
* Use `git diff HEAD~1` to review what the previous commit changed.
* Deliberately create a merge conflict in two branches, then resolve it.
* Add a `README.md` and see how GitHub renders it on the repo's home page.

---

### Summary Checklist

1. Repetition is the point: init → add → commit → branch → merge → push → clone.
2. `git commit -am` is the shortcut for tracked files.
3. Confirm the ignore rules actually kept the secret out.
4. Extra drills: revert, diff, conflict resolution, README.
