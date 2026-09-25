Here is a structured breakdown of this lesson on picking your terminal.

---

### 1. You Need a Terminal

Everything today happens on the command line: `git init`, `git add`, `git commit`,
`git push`. Which app hosts it matters far less than being comfortable in it.

---

### 2. The Options

| Setup | Terminal | Notes |
|-------|----------|-------|
| **VS Code** | integrated terminal (`Ctrl/Cmd + ~`) | easiest to follow along; Git Bash supported on Windows |
| **PyCharm** | *Terminal* tab at the bottom | handy if you're already coding in it |
| **macOS** | Terminal.app / iTerm (zsh) | Bash and zsh pre-installed |
| **Windows** | Git Bash (installed with Git) | gives you Unix commands + Git in one shell |

---

### 3. Why Git Bash on Windows?

Command Prompt can't run most Unix commands from this course (`ls`, `touch`, `pwd`,
`rm -rf`) and its Git experience is weaker. Git Bash gives you both.

---

### 4. Make It the Default

In VS Code:

1. *View → Command Palette* (`Ctrl/Cmd + Shift + P`).
2. Type **Select Default Profile**.
3. Choose **Git Bash**.
4. Close and reopen the terminal — the dropdown menu (next to `+`) should read *bash*.

In PyCharm, the bottom *Terminal* tab is already a shell; on Windows it uses `cmd` unless
you point *Settings → Tools → Terminal → Shell path* at `bash.exe`.

---

### 5. Quick Sanity Check

```bash
pwd                 # where am I?
git --version       # is Git installed and reachable?
```

If `git --version` prints a version, you're ready for the rest of the module.

---

### Summary Checklist

1. Any terminal works; VS Code's is the easiest to follow along with.
2. Windows users: Git Bash, not Command Prompt.
3. Set Git Bash as VS Code's default profile for new terminals.
4. Confirm with `git --version` before starting.
