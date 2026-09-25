Here is a structured breakdown of this challenge lesson on Jinja + APIs.

---

### 1. agify + genderize

Two no-auth APIs predict a name's age and gender:

```
https://api.agify.io/?name=angela      → {"name":"angela","age":49,"count":...}
https://api.genderize.io/?name=angela  → {"name":"angela","gender":"female",...}
```

---

### 2. The Challenge Route

```python
import requests

@app.route("/guess/<name>")
def guess(name):
    age_response = requests.get(f"https://api.agify.io?name={name}")
    gender_response = requests.get(f"https://api.genderize.io?name={name}")
    return render_template("guess.html",
                           person_name=name.title(),
                           age=age_response.json()["age"],
                           gender=gender_response.json()["gender"])
```

The server fetches, the template displays: `<h1>Hey {{ person_name }}, I guess
you're {{ age }}</h1>`. This exact pattern — *API → server → template* — is the
heart of every Flask app in the coming days.

---

### Summary Checklist

1. Route fetches from API, renders template with the results.
2. Day 32's requests skills + today's Jinja = dynamic data pages.
