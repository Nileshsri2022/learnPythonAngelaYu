# DataFrames & Series- Working with Rows & Columns

---

### 1. The Two Core Objects

```python
import pandas as pd

data = pd.read_csv("weather_data.csv")
```

* **DataFrame** — the whole table: `data` (has `.to_dict()`, `.to_csv()`, …)
* **Series** — one column: `data["condition"]`

```python
data_dict = data.to_dict()          # DataFrame → dict of columns
data_list = data["temp"].to_list()  # Series → plain Python list
```

---

### 2. Selecting Data

```python
print(data["temp"])                # by column name — recommended
print(data.temp)                   # attribute syntax (works if no spaces)

print(data[data.day == "Monday"])  # a ROW as a filtered DataFrame
print(data[data.temp == data.temp.max()])   # the hottest day
```

And computing on columns:

```python
monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
monday_f = monday_temp * 9 / 5 + 32     # convert to Fahrenheit
```

---

### 3. Creating a DataFrame from Scratch

```python
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65],
}
new_df = pandas.DataFrame(data_dict)
new_df.to_csv("new_data.csv")       # save it out
```

---

### Summary Checklist

1. DataFrame = table; Series = column.
2. Filter rows with `df[df.column == value]`.
3. Build DataFrames from dicts and export with `.to_csv()`.
