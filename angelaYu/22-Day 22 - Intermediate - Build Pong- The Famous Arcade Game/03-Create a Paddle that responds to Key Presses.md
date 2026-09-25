# Create a Paddle that responds to Key Presses

---

### 1. A Rectangle Paddle

Turtles are square by default — stretch one into a paddle:

```python
from turtle import Turtle, Screen

paddle = Turtle("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)   # 20×100
paddle.penup()
paddle.goto(350, 0)

screen = Screen()
screen.listen()

def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)

def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)

screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.exitonclick()
```

* `shapesize(stretch_wid=5, stretch_len=1)` — 5× vertical, 1× horizontal (20px base
  square → 20 wide, 100 tall).
* Movement keeps x fixed and changes **only y** — the paddle slides along its edge.

---

### Summary Checklist

1. Paddle = stretched square turtle at x = ±350.
2. Up/down = adjust `ycor()` by 20, keep `xcor()`.
3. Key bindings exactly like Day 19/20.
