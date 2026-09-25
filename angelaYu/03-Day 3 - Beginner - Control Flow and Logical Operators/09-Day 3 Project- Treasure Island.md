Here is a structured breakdown of the Day 3 final project — Treasure Island.

---

### 1. What the Program Does

A **choose-your-own-adventure** game. The story branches on three choices:

1. **Crossroad** — type `left` or `right` (right → fall into a hole, Game Over).
2. **Lake** — type `wait` for a boat or `swim` across (swim → attacked by a trout, Game Over).
3. **House with three doors** — `red` (fire), `blue` (beasts), `yellow` (**You Win!**).

```
You're at a crossroad. Where do you want to go? Type "left" or "right"
left
You've come to a lake. There's an island in the middle of the lake.
Type "wait" to wait for a boat. Type "swim" to swim across.
wait
You arrive at the island unharmed. There's a house with 3 doors.
One red, one yellow and one blue. Which colour do you choose?
yellow
You Win!
```

---

### 2. Key Techniques Used

* Nested `if`/`elif`/`else` — each choice opens the next stage *only if* the previous was correct.
* `.lower()` on the input so `"Left"` and `"left"` both work.
* Your own story wording — make it yours!

---

### 3. Solution Skeleton

```python
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input('You\'re at a crossroad. Where do you want to go? '
                'Type "left" or "right"\n').lower()
if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There\'s an island in the middle of the lake. '
                    'Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There's a house with 3 doors. "
                        "One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
```

> **Tip:** Track the nesting carefully — every new stage is one indentation level
> deeper, *inside* the branch that led to it.

---

### Summary Checklist

1. Three sequential choices → three levels of nested conditionals.
2. `.lower()` makes the game forgiving about letter case.
3. Full runnable version: [`treasure_island.py`](treasure_island.py)
