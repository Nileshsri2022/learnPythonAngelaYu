# Printing to the Console in Python

---

### 1. The `print()` Function

The whole point of programming is to **tell the computer what to do**. The first way we do
that is with the `print()` **function** — the word `print` in lowercase followed by parentheses:

```python
print("Hello world!")
```

* The **text inside the parentheses** is what gets printed.
* Text like `"Hello world!"` is a **string** — it must be wrapped in quotes.
* After running, the console shows your output and ends with
  **`Process finished with exit code 0`** — *exit code 0* means everything ran successfully.

---

### 2. Reading the Console Output

The output pane has three parts:

1. **First line** — the location of the file you just ran.
2. **Middle lines** — the result of your commands (your program's output).
3. **Last line** — `Process finished with exit code 0` on success, or an error message if something went wrong.

> **Tip:** In PyCharm, keep the run configuration set to **Current File** so the play
> button always runs the file you're editing. Keyboard shortcut: `Ctrl + R` (Mac).

---

### 3. Printing Multiple Lines

Calling `print()` once prints one line, so three lines need three calls:

```python
print("Hello world!")
print("Hello world!")
print("Hello world!")
```

---

### 4. Comments

A **comment** is a line Python completely ignores — it starts with the hash `#`:

```python
# This line is a comment. Python will not run it.
print("Hello world!")  # comments can also go at the end of a line
```

Use comments to leave notes for yourself (or other programmers) about *what the code does and why*.

---

### 5. Watch Out: Strings and Quotes

The quotes around a string must be a **matching pair**. This breaks:

```python
print("Hello world!)   # SyntaxError: unterminated string
```

And this breaks too, because the second `"` closes the string early:

```python
print("Hello "world!")  # SyntaxError
```

> **Note:** If a line is underlined in red, Python has spotted a **SyntaxError** —
> the code doesn't follow the rules of the language. Read the message; it usually
> tells you exactly what's wrong.

---

### Summary Checklist

1. `print()` outputs text to the console; text must be inside quotes.
2. `exit code 0` = success; anything else = something went wrong.
3. `#` starts a comment that Python ignores.
4. Unmatched or nested quotes cause a **SyntaxError**.
