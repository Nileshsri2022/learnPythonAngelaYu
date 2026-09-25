Here is a structured breakdown of this lesson on the goals for Day 49.

---

### 1. The Problem: Bookings Sell Out at Midnight

Meeting rooms, tennis courts, spin classes — the booking window always opens when you're
asleep, and by morning everything is gone. Today we automate the whole thing with Selenium.

---

### 2. The Practice Gym: "Snack & Lift"

The course ships a **gym website that runs entirely in your browser** — no server needed.

| Piece | Detail |
|-------|--------|
| Database | **IndexedDB** inside Chrome (DevTools → Application → Storage) |
| Test user | `student@test.com` / `password123` |
| Admin user | extra control panel over classes, bookings, users |
| "Clear Bookings only" | wipes bookings, keeps users |
| "Reset All Data" | back to the factory state — run this *before every bot run* |

> **Note:** Because the database lives in the browser, a **different Chrome profile sees a
> different database**. Registering or booking in one profile has no effect on another.

---

### 4. Why the Chrome Profile Matters

The bot must always use the **same Chrome profile**, or it will look at an empty database
(and have to log in again). Most people have one profile — if you have several, pick the
right one.

---

### 5. Simulators for Testing

Two toggles exist purely for quality assurance:

* **Time simulation** — pretend a day has passed, so you can test "book the *upcoming*
  Tuesday" logic without waiting a week.
* **Network simulation** — make requests fail occasionally, so you can prove your
  retry logic actually works.

> Turn network simulation **off** while developing, then on at the end for the resilience
> challenge.

---

### 6. Skills You'll Practise

* Persistent browser profiles (the bot "remembers" who it is).
* Handling content that depends on today's date.
* Dealing with button states: *available*, *full*, *already booked*, *waitlisted*.
* Retry logic implemented with **function wrappers / higher-order functions**.
* QA: verifying the bookings really landed on the *My Bookings* page.

---

### 7. The Shape of the Build

Start simple — log in and book one class — then grow: multiple classes, both weekdays,
counters, verification, time-travel QA and finally network resilience.

---

### Summary Checklist

1. Reset the browser database before each run; always reuse the same Chrome profile.
2. `student@test.com` / `password123` gets you a working account.
3. Time + network simulators exist for QA — leave them off until the end.
4. Final bot: logs in, books *next* Tuesday/Thursday classes, counts, verifies, retries.
