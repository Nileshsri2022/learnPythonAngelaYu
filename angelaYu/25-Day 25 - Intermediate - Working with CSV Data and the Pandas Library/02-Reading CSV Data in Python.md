Here is a structured breakdown of this lesson on reading CSV data.

---

### 1. What is a CSV?

**Comma-Separated Values** — a plain-text table. First row = column names; each following
line = a record:

```
temperature,day_of_week
12,Monday
14,Tuesday
15,Wednesday
```

---

### 2. Way 1 — The Built-in `csv` Module

```python
import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        temperatures.append(row[1])    # the "temperature" column
temperatures = temperatures[1:]        # drop the header row
```

* Rows arrive as lists of strings — you handle headers and type conversion yourself.

---

### 3. Way 2 — Pandas (much friendlier)

```bash
pip install pandas
```

```python
import pandas as pd

data = pd.read_csv("weather_data.csv")
print(data["temp"])        # the whole column, as numbers
```

Pandas parses headers, types and structure automatically — for real data work it's the
default choice.

---

### Summary Checklist

1. CSV = tables as text; commas split columns, newlines split rows.
2. `csv.reader` = manual but dependency-free.
3. `pd.read_csv` = instant, typed, labelled data.
