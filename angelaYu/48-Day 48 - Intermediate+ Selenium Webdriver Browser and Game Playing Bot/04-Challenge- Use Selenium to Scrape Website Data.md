# Challenge- Use Selenium to Scrape Website Data

---

### 1. The Challenge

Scrape the **Upcoming Events** section of python.org (dates + event names) and print a
dictionary in this shape:

```python
{
  0: {"time": "2020-04-17", "name": "PyCon Japan 2020"},
  1: {"time": "2020-04-27", "name": "PyCon US 2020"},
  ...
}
```

The events themselves are time-dependent — the structure matters, not the values.

---

### 2. Meet the Elements

Inspecting the page shows:

```html
<div class="event-widget">
  <ul>
    <li>
      <time datetime="2020-04-17">April 17</time>
      <a href="...">PyCon Japan 2020</a>
    </li>
    ...
  </ul>
</div>
```

`<time>` and `<li>` also appear in the *Latest News* widget — only `event-widget` is unique
to the section we want, so the selector must start there.

---

### 3. Scrape All Dates

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.python.org/")

event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
for time in event_times:
    print(time.text)
```

* `find_elements` (plural) returns every match as a list.
* `.event-widget time` = "every `<time>` inside the event widget".

---

### 4. Scrape All Names — with a Twist

The naive selector `.event-widget a` also grabs the widget's *More* link, because it is an
anchor tag too. Narrow it down: the event names live inside `<li>` elements.

```python
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
for name in event_names:
    print(name.text)
```

---

### 5. Build the Dictionary

```python
events = {}
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }

print(events)
driver.quit()
```

Each key is the index; each value is a nested dictionary (nesting from Day 9).

> **Tip:** This is exactly the shape you'd `json.dump()` to a file or hand to another API —
> scrape once, use everywhere.

---

### Summary Checklist

1. Chrome DevTools first: find the unique wrapper (`.event-widget`) then drill down.
2. `find_elements` + CSS selector gives you the whole list of matches.
3. Over-broad selectors catch extra anchors — add `li` to filter them out.
4. Loop `range(len(list))` to pair two parallel lists into a nested dictionary.
