Here is a structured breakdown of this lesson on controlling the snake with keypresses.

---

### 1. Binding the Arrow Keys

Event listeners from Day 19, bound to direction changes:

```python
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
```

Arrow keys are named `"Up"`, `"Down"`, `"Left"`, `"Right"`.

---

### 2. The Direction Methods (inside `Snake`)

```python
def up(self):
    if self.head.heading() != DOWN:
        self.head.setheading(UP)

def down(self):
    if self.head.heading() != UP:
        self.head.setheading(DOWN)

def left(self):
    if self.head.heading() != RIGHT:
        self.head.setheading(LEFT)

def right(self):
    if self.head.heading() != LEFT:
        self.head.setheading(RIGHT)
```

With module constants:

```python
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
```

* `self.head` — the first segment (`self.segments[0]`), exposed as an attribute.
* The `if` check prevents the snake from doing a 180° U-turn into its own neck —
  the player could only move in a direction perpendicular (or parallel) to travel.

> **Note:** Turning doesn't move the snake — `move()` still handles motion; keys only
> change `heading`. That separation keeps control crisp.

---

### Summary Checklist

1. `screen.listen()` + four `onkey` bindings.
2. Direction methods set `heading()` on the **head** segment.
3. Block 180° reversals with a heading check.
