# String Manipulation and Code Intelligence

---

### 1. New Lines with `\n`

Instead of calling `print()` several times, a single `print()` can produce several lines
using the **escape character `\n`** (backslash + n):

```python
print("Hello world!\nHello world!\nHello world!")
```

**Output:**
```text
Hello world!
Hello world!
Hello world!
```

* It's a **backslash `\`**, not a forward slash `/`.
* Write `\n` with **no spaces** around it unless you actually want a space in the output.

---

### 2. String Concatenation

**Concatenation** means combining strings — joining one string onto the end of another with
the `+` sign:

```python
print("Hello" + "Angela")
```

**Output:**
```python
HelloAngela
```

There is no space because there is no space *character* in either string. To get one:

```python
print("Hello " + "Angela")   # space at the end of the first string
print("Hello" + " " + "Angela")  # a " " string in between
```

**Output:**
```text
Hello Angela
Hello Angela
```

Think of a string as a *string of connected characters* — concatenation just merges the two
strings into one longer string.

---

### 3. Spaces Matter in Python

Python is picky about spaces:

* Extra spaces **inside** strings show up in the output.
* Extra spaces around **syntax** (like `print ( )`) can change meaning or cause errors.

---

### 4. Code Intelligence (Autocomplete)

As you type, the editor's **code intelligence** suggests completions for function names and
shows their expected parameters. It speeds you up and prevents typos — use it, don't fight it.

---

### Summary Checklist

1. `\n` creates a new line **inside** a single string.
2. `+` concatenates (joins) strings; spaces only exist if you add them.
3. Python cares about spaces — both in strings and around syntax.
4. Code intelligence autocompletes and documents functions as you type.
