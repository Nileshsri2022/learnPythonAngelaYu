# Install Git Bash on Windows

---

### 1. macOS?

Bash/zsh and Git are already there — skip this lesson and go straight to version control.

---

### 2. Install Git for Windows

1. Download the installer from **gitforwindows.org** (Git SCM).
2. Run it → *Yes* to the User Account Control prompt.
3. Accept the licence → **Next**.
4. Choose the install location → **Next**.
5. Select components: **make sure "Git Bash" is checked**.
6. Leave every other screen at its default and keep clicking **Next**.
7. Finish.

The defaults are fine — the one setting that matters is the Git Bash checkbox.

---

### 3. Verify It Works

Open VS Code → *Terminal → New Terminal* → click the dropdown next to `+` → **Git Bash**.

You should see a `$` prompt. Then:

```bash
git --version     # e.g. git version 2.45.1.windows.1
```

---

### 4. Make Git Bash the Default Shell

1. *View → Command Palette* (`Ctrl + Shift + P`).
2. **Select Default Profile** → **Git Bash**.
3. Close the current terminal and open a new one — the profile should now say *bash*.

Now every new terminal starts in Git Bash, with `ls`, `touch`, `pwd` and `git` all
available.

---

### Summary Checklist

1. Git for Windows ships Git **and** Git Bash — keep the Git Bash component checked.
2. Defaults are safe; just click through.
3. Verify with `git --version` inside a Git Bash terminal.
4. Set Git Bash as VS Code's default profile so every new terminal uses it.
