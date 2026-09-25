# Indentation in Python

---

### 1. Indentation Defines Blocks

After any line ending in a colon (`def`, `if`, `for`, `while`…), the lines **shifted right
by 4 spaces** belong to that block:

```python
def my_function():
    print("Hello")     # inside the function
    print("World")     # inside the function

print("Outside")       # NOT inside — runs immediately, not on call
```

* Inside → executes *as part of* the function.
* Outside → completely independent code.

---

### 2. The Folder Analogy

Think of indentation like **folders in Finder / File Explorer**:

* A function is a **folder** (`my_function/`).
* Indented lines are **files inside the folder**.
* Un-indent a line and you've dragged it *out* of the folder — it no longer lives there.

```python
def my_function():
    print("Hello")
print("World")    # outside the "folder"
```

---

### 3. Nesting = Deeper Indentation

Blocks inside blocks just indent further:

```python
def my_function():
    for n in range(3):          # level 1 — inside the function
        if n % 2 == 0:          # level 2 — inside the loop too
            print(n)            # level 3
```

> **Warning:** In Python, indentation is **syntax**, not decoration (unlike most
> languages where it's cosmetic). Wrong indentation = different meaning or an
> `IndentationError`.

---

### Summary Checklist

1. After a colon, an indented block belongs to that construct.
2. Visualise an invisible border around every indented block.
3. Deeper nesting = deeper indentation; keep it consistent (4 spaces).
