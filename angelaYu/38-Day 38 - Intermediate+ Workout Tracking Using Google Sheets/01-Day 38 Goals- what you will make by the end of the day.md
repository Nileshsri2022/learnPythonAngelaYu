# Day 38 Goals: what you will make by the end of the day

A challenge project with a twist: log your workout in **plain English** and let a
natural-language API fill in a **Google Sheet** for you.

---

### 1. The Inspiration

OpenAI's GPT-3 can answer *"why is bread so fluffy?"* by understanding a Wikipedia
article — that is **natural language processing** (NLP). This project uses the same
idea (via Nutritionix) so you never type a table of exercises yourself.

---

### 2. How It Works

You type one sentence — *"ran 5K and cycled for 20 minutes"* — and the program:

| Step | Result |
|------|--------|
| Understand the exercise name | `running`, `cycling` |
| Duration | from the distance (5K ≈ **31 min**), or from your own words (*20 min*) |
| Calories | calculated from **gender, age, weight, height** you configured |
| Save the row | Sheety appends date/time, exercise, duration and calories to a Google Sheet |

Workout, time, duration and "how many ice creams you earned" — all logged automatically.

---

### 3. Skills You Are Reusing

* `datetime.strftime()` — stamping each row with today's date and time
* **GET with headers** — POST/GET calls that need an `x-app-id`/`x-app-key` or
  `Authorization` header
* **POST requests** — sending the workout to Sheety to add a row
* **Environment variables** — keeping both API keys out of your code

And one new trick: run the Python REPL **on your phone's browser** so you can log a
workout right after the gym.

---

### Summary Checklist

1. Input = a normal English sentence; NLP parses the exercise, duration and calories.
2. Nutritionix turns "ran 5K" into duration and burned calories using your body data.
3. Sheety receives a POST and appends the row to a Google Sheet automatically.
4. Everything else is review: headers, POST, `strftime`, environment variables.
5. Do it yourself from the starter instructions — this is a challenge day.
