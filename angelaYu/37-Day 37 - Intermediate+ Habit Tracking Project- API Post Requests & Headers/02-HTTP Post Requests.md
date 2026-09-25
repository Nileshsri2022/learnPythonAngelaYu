Here is a structured breakdown of this lesson on POST requests.

---

### 1. GET vs. POST

* **GET** — *retrieve* data; parameters ride in the URL.
* **POST** — *send* data to create something; the payload rides in the **body**.

```python
import requests

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "abc1234567890",
    "username": "yourname",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)
# {"message":"Success.","isSuccess":true}
```

* `json=` — requests serialises the dict into the request body and sets the
  content-type header for you.

---

### Summary Checklist

1. POST = create; body carries the payload as JSON.
2. The response text tells you whether the API accepted it.
