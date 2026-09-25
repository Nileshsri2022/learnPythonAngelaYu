Here is a structured breakdown of this lesson on import styles and aliases.

---

### 1. The Three Ways to Import

```python
# 1. Import the whole module — use module.name
import turtle
timmy = turtle.Turtle()

# 2. Import specific names — use them directly
from turtle import Turtle
timmy = Turtle()

# 3. Import with an alias — shorten noisy names
import turtle as t
timmy = t.Turtle()
```

All three run the same code; they differ in **namespacing and readability**.

---

### 2. Which to Use?

| Style | Good for | Watch out |
|-------|----------|-----------|
| `import module` | clarity about where names come from | verbose |
| `from module import name` | frequent use of a few names | name collisions |
| `import module as alias` | long names (`as t`, `as pd`, `as plt`) | obscure if overused |

> **Warning:** `from turtle import *` imports *everything* into your namespace — it
> makes code hard to trace. Avoid it.

---

### Summary Checklist

1. Three import styles: module, named, aliased.
2. Aliases are convention (`t`, `pd`, `plt`) — learn to recognise them.
3. Prefer explicit imports; skip `import *`.
