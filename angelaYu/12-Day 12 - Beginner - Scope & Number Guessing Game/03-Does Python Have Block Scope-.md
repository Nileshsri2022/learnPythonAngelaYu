Here is a structured breakdown of everything covered in this lesson on block scope.

---

### 1. Python Has No Block Scope

Coming from Java, C++ or JavaScript, you'd expect `if`/`for`/`while` blocks to create a new
scope. **In Python they don't** — only **functions** create local scope:

```python
if 3 > 2:
    a_variable = 10        # not local to the if — this is GLOBAL

print(a_variable)          # 10 — perfectly legal (and dangerous!)
```

The same applies to variables created in `for` and `while` loops — they exist after the
loop ends.

---

### 2. The Practical Consequence

* Variables "leak" out of blocks — which is convenient but can hide bugs.
* Two different `if` branches can accidentally overwrite each other's variables.
* Rule of thumb: **declare loop/block variables before the block** when you plan to use
  them afterwards, and keep genuinely temporary data inside functions.

---

### Summary Checklist

1. In Python, `if` / `for` / `while` do **not** create scope.
2. Only `def` (and `lambda`/comprehensions, later) create local namespaces.
3. Don't rely on it — structure code so variables live where they're used.
