# How to use HTTP Put and Delete Requests

Yesterday's pixel was wrong — or shouldn't exist at all. The remaining two HTTP verbs
fix both mistakes.

---

### 1. Only the Method Changes

```python
requests.post(url, json=..., headers=...)      # create
requests.put(url, json=..., headers=...)       # update
requests.delete(url, headers=...)              # remove — no body needed
```

---

### 2. Update a Pixel: `PUT`

The update endpoint is the pixel endpoint **plus the date** you are changing:

```python
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday}"
new_pixel_data = {"quantity": "4.5"}           # "I lied about 15 km"

response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
print(response.text)
```

* Only the field you want to change belongs in the body — here, just `quantity`.
* The date in the URL is what selects the pixel.
* Watch your quotes when you f-string an already-quoted variable; mixing `"` and `'`
  keeps Python happy.

Refresh the graph: yesterday's square becomes lighter, because 4.5 km is less than the
15 km it held before.

---

### 3. Delete a Pixel: `DELETE`

Same URL, no body, headers still required for authentication:

```python
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday}"

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
```

A `Success` message means the pixel is gone — refresh and the square has vanished.

---

### 4. Finish the Project

Turn the script into a tool you actually use:

1. Comment out the user/graph/put/delete calls — keep only the pixel poster.
2. Ask for the value instead of hard-coding it:

```python
quantity = input("How many kilometres did you cycle today? ")
pixel_data = {"date": datetime.now().strftime("%Y%m%d"), "quantity": quantity}
requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
```

3. (Pixela rejects a second pixel for the same date — that is a feature, not a bug.)
4. Adapt it to *your* habit: pages read, minutes meditated, lengths swum.

---

### Summary Checklist

1. `PUT` updates, `DELETE` removes; both reuse the same URL pattern as POST.
2. The date at the end of the URL picks the pixel to change or delete.
3. PUT sends only the changed field (`quantity`); DELETE sends no body.
4. Both still need `headers={"X-USER-TOKEN": TOKEN}`.
5. Ship it: swap the hard-coded value for `input()`, keep `strftime` for today's date.
6. One pixel per date — post today's data tomorrow, or update yesterday's pixel.
