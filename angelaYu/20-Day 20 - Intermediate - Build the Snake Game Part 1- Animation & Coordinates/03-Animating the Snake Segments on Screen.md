# Animating the Snake Segments on Screen

---

### 1. Making the Snake Move

To move the whole snake **forward**, each segment steps into the position of the segment
in front of it — then the head advances:

```python
game_is_on = True
while game_is_on:
    screen.update()            # render one frame
    time.sleep(0.1)            # wait 0.1s — the frame delay

    for seg_num in range(len(segments) - 1, 0, -1):     # last → first
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)    # head moves on
```

---

### 2. Why Loop in *Reverse*?

If the head segment moved first, each following segment would copy its *already-moved*
predecessor and the whole snake would bunch up. Moving **tail → head** means every segment
copies where its leader *was* this frame — the classic snake follow-the-leader.

* `range(len - 1, 0, -1)` — from the last index down to 1 (the start is excluded).
* `screen.update()` + `time.sleep(0.1)` produce the frame loop instead of `tracer`'s
  automatic drawing.

---

### Summary Checklist

1. Game loop = update → sleep → move segments → repeat.
2. Move segments **backwards through the list**, then the head forward.
3. Reversing the iteration order is the entire snake-follow mechanic.
