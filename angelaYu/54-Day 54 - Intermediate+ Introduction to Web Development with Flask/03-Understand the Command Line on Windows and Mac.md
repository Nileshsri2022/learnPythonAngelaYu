Here is a structured breakdown of this lesson on the command line.

---

### 1. Why Use the Terminal at All?

Everything the GUI does, the terminal can do — with more control and often less effort
once you know the commands. PyCharm bundles the same terminal (`zsh` on macOS, Command
Prompt on Windows) at the bottom of the window.

---

### 2. The Essential Commands

| Command | Meaning | Notes |
|---------|---------|-------|
| `pwd` | **p**rint **w**orking **d**irectory | where am I? |
| `ls` | **l**i**s**t files here | everything in Finder, in text |
| `cd Desktop` | **c**hange **d**irectory | move into a folder |
| `cd ..` | up one level | `..` = parent folder |
| `mkdir Test` | **m**a**k**e **dir**ectory | create a folder |
| `touch main.py` | create an (empty) file | any extension works |
| `rm main.py` | **r**e**m**ove a file | no trash, no confirmation |
| `rm -rf Test` | remove a *folder* recursively & forcefully | dangerously powerful |

Windows equivalent of `export` is `set`; the rest are largely identical.

---

### 3. Tab Completion Is Your Friend

Type the first letters of a path and press **Tab** — the shell completes it, narrowing
options as you type (`cd De` + Tab → `Development/` or `Desktop/`). It saves keystrokes
*and* prevents typos.

---

### 4. `rm -rf` Deserves Respect

* Recursive: deletes the folder **and everything inside it**.
* Forceful: no confirmation prompt, no recycle bin.
* Aimed at the wrong path — say, your home directory — it is a genuine disaster story you
  can find all over the internet.

> **⚠️ Warning:** Always `pwd` first and double-check the folder name before an
> `rm -rf`. With great power comes great responsibility.

---

### 5. Cheatsheets

Search "terminal cheatsheet" or "command prompt cheatsheet" for the long tail. The
commands above cover the overwhelming majority of day-to-day use — and they're exactly
what you need to run your Flask server, install packages with `pip` and set environment
variables.

---

### Summary Checklist

1. `pwd`, `ls`, `cd`, `mkdir`, `touch`, `rm` — the daily five (plus `cd ..`).
2. Tab completion completes paths for you.
3. macOS default shell is `zsh`; Windows is Command Prompt.
4. `rm -rf` is permanent — check your location twice.
5. `export` (Mac) / `set` (Windows) define environment variables like `FLASK_APP`.
