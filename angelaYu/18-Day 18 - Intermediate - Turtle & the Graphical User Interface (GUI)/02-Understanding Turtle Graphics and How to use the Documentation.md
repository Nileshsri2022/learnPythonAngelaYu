Here is a structured breakdown of this lesson on Turtle graphics and reading documentation.

---

### 1. Turtle Basics

Turtle is Python's built-in drawing module — a robot turtle with a pen:

```python
import turtle

timmy = turtle.Turtle()      # the pen
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)           # draw a line 100px

my_screen = turtle.Screen()  # the window
print(my_screen.canvwidth)
my_screen.exitonclick()      # keep the window open until clicked
```

---

### 2. Reading the Docs — the Real Lesson

The lecture's purpose is teaching you to **use the official documentation** at
docs.python.org/3/library/turtle.html:

* The method list looks overwhelming — scan the **names** first.
* Each method's page shows the signature and an example.
* Professional programmers read docs daily; memorising APIs is impossible and unnecessary.

> **Tip:** In PyCharm, hovering shows the same docs. `dir(obj)` and `help(obj)` are the
> offline shortcuts.

---

### Summary Checklist

1. `Turtle()` = pen object; `Screen()` = canvas object.
2. `forward/ backward/ right/ left/ color/ shape/ penup/ pendown` are the core moves.
3. Learn to *look things up* — that's the durable skill.
