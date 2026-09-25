# Git & GitHub Cheat Sheet (Day 70)

A one-page reference for everything covered in the Git, GitHub and Version Control module.

---

## 1. Set up

```bash
git --version                    # is Git installed?
git config --global user.name  "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
```

---

## 2. Start a repository

```bash
git init                         # create a repo in the current folder
git clone <url>                  # copy an existing repo (with full history)
git status                       # what's untracked / staged / modified
ls -a                            # show the hidden .git folder
```

---

## 3. The everyday loop

```bash
git add file.txt                 # stage one file
git add .                        # stage everything here
git commit -m "Add chapter 1"    # save point with a message
git commit -am "Fix typo"        # stage+commit tracked files only
```

```text
working directory --(add)--> staging area --(commit)--> history
```

---

## 4. Inspect

```bash
git log                          # full history
git log --oneline                # one line per commit
git diff                         # unstaged changes
git diff --staged                # staged changes
git show <hash>                  # what a specific commit changed
git check-ignore -v secrets.txt  # which .gitignore rule matched?
```

---

## 5. Undo

```bash
git restore file.txt             # discard unstaged edits to a file
git checkout <hash> -- file.txt  # bring back one file from an old commit
git reset --soft HEAD~1          # undo last commit, keep the changes staged
git revert <hash>                # new commit that undoes an old one (safe when pushed)
git reset --hard <hash>          # ⚠️ discard everything after <hash>
```

---

## 6. Remotes (GitHub)

```bash
git remote add origin <url>      # connect local repo to GitHub
git remote -v                    # list remotes
git push -u origin main          # first push; -u remembers the pairing
git push                         # upload commits
git pull                         # download + merge commits
```

---

## 7. Branches and merges

```bash
git branch                       # list (* = current)
git checkout -b feature-x        # create + switch
git switch -c feature-x          # modern equivalent
git checkout main                # switch back
git merge feature-x              # merge into the current branch
git branch -d feature-x          # delete after merging
```

Conflicts: edit the file, remove `<<<<<<<`, `=======`, `>>>>>>>`, then `git add` +
`git commit`.

---

## 8. Fork & pull request

```bash
# fork on GitHub, then:
git clone https://github.com/YOU/project.git
git checkout -b fix-typo
git commit -am "Fix typo in README"
git push -u origin fix-typo
# open the PR on GitHub

# keep your fork up to date
git remote add upstream https://github.com/ORIGINAL/project.git
git fetch upstream
git merge upstream/main
```

---

## 9. `.gitignore` starters

```gitignore
# secrets
.env
secrets.txt

# macOS / Windows
.DS_Store
Thumbs.db

# Python
__pycache__/
*.pyc
venv/
.venv/

# local data
instance/
*.db
```

Already committed a secret? `git rm --cached secrets.txt`, add it to `.gitignore`,
commit — and **rotate the credential**.

---

## 10. Commit messages that help future-you

| ❌ | ✅ |
|----|----|
| "stuff" | "Add user registration route" |
| "fixed it" | "Fix off-by-one error in pagination" |
| "final" | "Update README install instructions" |

Imperative mood, one logical change per commit, and a body explaining *why* when the
reason isn't obvious.
