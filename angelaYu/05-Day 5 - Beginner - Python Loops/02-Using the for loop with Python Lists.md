Here is a structured breakdown of everything covered in this lesson on looping through Python lists with the `for` loop.

---

### 1. What is a Loop?

A **loop** is a way to make something happen over and over and over again. Instead of writing the same line of code many times by hand, we tell the computer to repeat it for us — saving time and energy.

The first type of loop introduced here is the **`for` loop**, which combines perfectly with **Lists** from the previous lesson: it lets us go through each item in a list and perform an action with each individual item.

---

### 2. The `for` Loop with Lists

Say we have a list of fruits and want to print each one individually:

```python
fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
```

**Output:**
```
Apple
Peach
Pear
```

Breaking the syntax down piece by piece:

* **`for`** — the keyword that starts the loop.
* **`fruit`** — a name we invent for *a single item* in the list.
* **`in`** — the keyword that connects the item name to the collection.
* **`fruits`** — the list we want to loop through.
* **`:`** — the colon that ends the loop header; the next line **must be indented**.

---

### 3. What Happens Behind the Scenes

Imagine the loop assigning the variable `fruit` to each item in turn:

1. **1st iteration:** `fruit = "Apple"` → `print(fruit)` prints `Apple`
2. **2nd iteration:** `fruit = "Peach"` → `print(fruit)` prints `Peach`
3. **3rd iteration:** `fruit = "Pear"` → `print(fruit)` prints `Pear`

> **Tip:** Step through this in the **Thonny IDE** with the debug icon to watch the
> `fruit` variable attach to `"Apple"`, then `"Peach"`, then `"Pear"`, one step at
> a time — the clearest way to see how the loop really works.

---

### 4. Executing a Whole Block of Statements

A `for` loop is **not limited to a single statement** — everything that is indented after the colon is *inside* the loop and runs once per item:

```python
fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
```

**Output:**
```
Apple
Apple pie
Peach
Peach pie
Pear
Pear pie
```

Each pass through the loop body prints the fruit **and** the fruit + " pie" before moving to the next item.

---

### 5. Inside vs. Outside the Loop (Indentation!)

Whenever you see a **colon** — in `if` statements or `for` loops — the **indentation** that follows decides what is inside that block:

```python
fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    print(fruits)   # INSIDE: printed 3 times (once per item)

print("Loop is done")  # OUTSIDE: printed once, after the loop finishes
```

* **Indented** → runs once *for every item* in the list.
* **Not indented** → runs *only once*, after the whole loop has finished.

> **Warning:** Indentation is really, really important. Be careful with it —
> moving a single line in or out of the loop completely changes the output.

---

### Summary Checklist

1. **Purpose:** Loops execute the same code multiple times without repeating it by hand.
2. **Syntax:** `for single_item in list_name:` — then indent the body.
3. **Loop variable:** `fruit` is reassigned to each list item in order, every iteration.
4. **Loop body:** Everything indented under the `for` runs once per item — one or many statements.
5. **Indentation decides scope:** indented = inside the loop (repeats); unindented = outside (runs once, at the end).
