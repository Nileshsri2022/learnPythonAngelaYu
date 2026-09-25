Here is a structured breakdown of the Day 37 goals — the Habit Tracker.

---

### 1. Skills Covered on Day 37

* **POST requests** — sending data *to* an API
* **HTTP headers** — advanced authentication (`X-USER-TOKEN`)
* **`strftime()`** — formatting today's date automatically
* **PUT and DELETE** — updating and removing resources

---

### 2. The Project: Pixel Habit Tracker

Using the [Pixela](https://pixe.la) API — a GitHub-style graph of coloured pixels:

1. Create a **user** (POST).
2. Create a **graph** for your habit (POST, token in a header).
3. Each day, POST a **pixel** (quantity) — auto-dated with `strftime`.
4. Update (PUT) or remove (DELETE) any pixel.

By the end, a chart like GitHub's contribution grid tracks your habit.

---

### Summary Checklist

1. GET reads; POST creates; PUT updates; DELETE removes — full CRUD.
2. Headers carry credentials without exposing them in URLs.
