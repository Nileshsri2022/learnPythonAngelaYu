Here is a structured breakdown of this lesson on the command line.

---

### 1. The Survival Set

| Task | Mac/Linux | Windows |
|---|---|---|
| list files | `ls` | `dir` |
| change directory | `cd folder` / `cd ..` | same |
| run Python | `python3 main.py` | `py main.py` |
| install packages | `pip3 install flask` | `pip install flask` |
| current location | `pwd` | `cd` (no args) |

---

### 2. Why It Matters for Flask

You start the server from the terminal (`python3 main.py`), and it keeps the terminal
hostage while running — **Ctrl+C** stops it. Server logs (every request, every error)
print right there.

> **Tip:** run the terminal from your project folder (PyCharm's Terminal tab opens it
> there automatically).

---

### Summary Checklist

1. ls/cd/python3/pip — the four commands you'll use hourly.
2. Ctrl+C stops a running server.
