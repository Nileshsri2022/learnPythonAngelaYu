Here is a structured breakdown of this lesson on fixing errors and watching for red underlines.

---

### 1. Tip #4: Fix Errors as They Appear

Don't pile new code on top of a broken state. **Red underlines** in the editor are errors
spotted *before* you even run; the console's error message is the runtime version of the
same advice.

```python
def greet(name)
    print(f"Hello {name}")     # red underline: missing colon → SyntaxError
```

---

### 2. Read the Traceback Bottom-Up

Python's error reports end with the **exception type and message** — read that last line
first:

```
Traceback (most recent call last):
  File "main.py", line 5, in <module>
    print(10 / 0)
ZeroDivisionError: division by zero
```

* **Line number** → where to look.
* **Exception type** → what category of mistake (`TypeError`, `NameError`, `IndexError`, …).
* **Message** → the specific detail.

Common starter exceptions: `SyntaxError`, `NameError`, `TypeError`, `IndexError`,
`KeyError`, `ValueError`, `ZeroDivisionError`.

---

### Summary Checklist

1. Red underline = fix before running; traceback = read the bottom line first.
2. Line number + exception type usually point straight at the fix.
3. Never build on a red-squiggled foundation.
