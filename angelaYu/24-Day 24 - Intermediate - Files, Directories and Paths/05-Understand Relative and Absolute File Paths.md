Here is a structured breakdown of this lesson on relative and absolute file paths.

---

### 1. Two Ways to Locate a File

```python
# Relative — starts from the current working directory
with open("data.txt") as file:
    ...

# Absolute — the full address from the disk root
with open("/Users/angela/Documents/data.txt") as file:
    ...
```

* **Relative** paths break when the script is run from a different working directory.
* **Absolute** paths break when the file moves to another machine.

---

### 2. The Robust Pattern

Anchor the path to the *script's own location*:

```python
import os

file_path = os.path.join(os.path.dirname(__file__), "data.txt")
with open(file_path) as file:
    ...
```

`os.path.dirname(__file__)` is the folder containing the running script — the file is
found no matter where the script is launched from.

> **Tip:** The course later introduces `pathlib` (`Path(__file__).parent / "data.txt"`)
> as the modern alternative — same idea, nicer syntax.

---

### Summary Checklist

1. Relative = from cwd (fragile); absolute = full address (unportable).
2. Anchoring to `__file__` makes file access robust.
3. Directories in paths: `folder/file.txt` (forward slash on all platforms in Python).
