Here is a structured breakdown of the Day 1 final project — the Band Name Generator.

---

### 1. What the Program Does

1. Prints a welcome message.
2. Asks **which city you grew up in**.
3. Asks **the name of a pet**.
4. Combines the two answers into a **band name** and prints it.

Example: city `Bristol` + pet `Rabbit` → band name **`Bristol Rabbit`**.

---

### 2. Building It Step by Step

**Step 1 — Greeting** with `print()`:

```python
print("Welcome to the Band Name Generator.")
```

**Step 2 — Ask for the city** with `input()`, and **store it in a variable** so it isn't lost:

```python
city = input("Which city did you grow up in?\n")
```

**Step 3 — Ask for the pet** the same way:

```python
pet = input("What is the name of a pet?\n")
```

**Step 4 — Combine and show the band name** using concatenation:

```python
print("Your band name could be " + city + " " + pet)
```

> **Tip:** Adding `"\n"` at the end of an input prompt puts the typing cursor on a
> new line — just like the reference program. A `" "` string in the final print
> keeps a space between the city and the pet.

---

### 3. Full Solution

```python
print("Welcome to the Band Name Generator.")
city = input("Which city did you grow up in?\n")
pet = input("What is the name of a pet?\n")
print("Your band name could be " + city + " " + pet)
```

**Sample run:**
```
Welcome to the Band Name Generator.
Which city did you grow up in?
Bristol
What is the name of a pet?
Rabbit
Your band name could be Bristol Rabbit
```

---

### Summary Checklist

1. `print()` for messages, `input()` with a prompt for questions.
2. **Save every answer in a variable** or it's gone.
3. Concatenate with `+`, adding `" "` where you need spaces.
4. Runnable version: [`band_name_generator.py`](band_name_generator.py)
