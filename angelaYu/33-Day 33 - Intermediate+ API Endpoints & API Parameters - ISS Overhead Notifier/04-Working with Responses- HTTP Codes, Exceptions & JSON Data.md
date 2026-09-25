Here is a structured breakdown of this lesson on response codes.

---

### 1. The HTTP Status Families

| Code | Meaning |
|------|---------|
| 1xx | Hold on / informational |
| 2xx | **Success** (200 OK) |
| 3xx | Go away / redirected |
| 4xx | **You screwed up** (404 not found, 403 forbidden) |
| 5xx | **I (the server) screwed up** (500) |

* [httpstatusdogs.com](https://httpstatusdogs.com) / [http.cat](https://http.cat) make
  them memorable.

---

### 2. Handling Bad Responses

```python
response = requests.get(url="https://api.example.com/endpoint")
response.raise_for_status()     # raises HTTPError for 4xx/5xx — catch it!

data = response.json()
```

Wrap risky calls in `try`/`except` (Day 30) when a failure should not crash your app:

```python
try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.HTTPError:
    print("The API is having a bad day.")
```

---

### Summary Checklist

1. 2xx good; 4xx your fault; 5xx theirs.
2. `raise_for_status()` = the network version of fail-loudly.
