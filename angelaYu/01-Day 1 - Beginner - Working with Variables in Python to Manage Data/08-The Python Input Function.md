Here is a structured breakdown of everything covered in this lesson on the Python input function.

---

### 1. The Problem: Getting Data *From* the User

`print()` sends data **out** to the console. But a program usually needs data **in** — like
asking "What is your name?" and letting the user type an answer. That is what the
**`input()`** function is for.

---

### 2. The `input()` Function

```python
input("What is your name?")
```

* Looks almost identical to `print()`, but…
* The text inside the parentheses is the **prompt** — a hint shown to the user about what to type.
* When it runs, the prompt is printed and the program **pauses**, showing a cursor, waiting for the user to type.

---

### 3. What the "Program is Waiting" State Looks Like

While `input()` is waiting, in PyCharm you'll notice:

* The **stop button** lights up and the play button becomes a **rerun** symbol.
* There's **no** `Process finished with exit code 0` line — the process hasn't finished!
* Click into the output pane, type your answer, press **Enter** — *now* the program continues and exits.

---

### 4. The Problem: The Data Disappears

Once you press Enter, the typed text is received by `input()`… and then **lost**, because we
never gave it a name:

```python
input("What is your name?")   # the answer is gone after Enter
```

The fix is the subject of the next lesson — store the result in a **variable**:

```python
name = input("What is your name?")
print(name)
```

> **Note:** Whatever the user types arrives as a **string**. Day 2 covers what that
> means when you want to do maths with it.

---

### Summary Checklist

1. `input(prompt)` prints the prompt and **waits** for the user to type + Enter.
2. The program only finishes (exit code 0) after the user has answered.
3. The answer is returned by `input()` — if you don't store it, it's lost.
4. Store it with `name = input(...)` so you can use it later.
