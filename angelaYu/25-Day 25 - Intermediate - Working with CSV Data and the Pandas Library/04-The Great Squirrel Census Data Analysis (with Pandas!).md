# The Great Squirrel Census Data Analysis (with Pandas!)

---

### 1. The Dataset

`2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv` — real volunteer data cataloguing
every squirrel spotted in Central Park, including fur colour.

---

### 2. The Task

Count squirrels by primary fur colour and output a small summary CSV:

```text
Fur Color,Count
gray,2473
red,392
black,103
```

---

### 3. Two Solutions

**With plain Pandas filtering:**

```python
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, red_count, black_count],
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
```

**With groupby (the one-liner way):**

```python
counts = data.groupby("Primary Fur Color").size()
```

* `len(df[condition])` — filter then count.
* `DataFrame(dict)` + `to_csv()` — the summary table out.

---

### Summary Checklist

1. Real datasets have messy column names — use bracket syntax for spaces.
2. Filter → len() is the simplest analysis pattern in Pandas.
3. Analysis isn't done until the result is saved somewhere.
