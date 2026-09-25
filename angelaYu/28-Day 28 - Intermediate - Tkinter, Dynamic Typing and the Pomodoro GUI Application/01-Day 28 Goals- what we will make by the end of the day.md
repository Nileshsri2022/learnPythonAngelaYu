Here is a structured breakdown of the Day 28 goals and the project you'll have built by the end of the day.

---

### 1. Skills Covered on Day 28

* The **Canvas** widget — images and text on a drawn background
* **Countdown mechanics** — `window.after()` for non-blocking timers
* **Dynamic typing** — how Python's types work at runtime (and how to tame them)

---

### 2. The Project: Pomodoro Timer

The productivity technique: 25 min work → 5 min break → repeat, with a longer break every
4th round. The app:

* Tomato timer face (image on canvas) counting down `MM:SS`.
* **Start / Reset** buttons; checkmarks ✔ show completed work sessions.
* Sessions alternate work/break automatically, colour-coded.

---

### Summary Checklist

1. Canvas = free-form drawing area; images and text live on it.
2. `after(ms, fn)` schedules callbacks without freezing the UI.
3. Dynamic typing pitfalls (int ↔ str) appear the moment a timer displays itself.
