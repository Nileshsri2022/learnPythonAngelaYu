# Step 7- Verify Class bookings on the -My Bookings- Page

---

### 1. Never Trust a Click

A click can land on a disabled button, a page can fail to save, a network hiccup can drop
the request. **Verification** — reading back the state — is what separates a script from a
reliable automation.

---

### 2. Navigate to *My Bookings*

```python
driver.get(f"{GYM_URL}/my-bookings")

booked_rows = driver.find_elements(By.CSS_SELECTOR, "div.booking-row")
for row in booked_rows:
    print(row.text)
```

---

### 3. Compare Expected vs Actual

```python
expected = {str(date) for date in targets_booked}     # dates we think we booked
actual = set()

for row in booked_rows:
    date_text = row.find_element(By.CSS_SELECTOR, ".booking-date").text
    actual.add(date_text.strip())

missing = expected - actual          # booked but not listed  → failure
extra   = actual - expected          # listed but not booked  → unexpected

print(f"Verified {len(expected & actual)}/{len(expected)} bookings")
if missing:
    print("MISSING:", sorted(missing))
```

* Sets (Day 5/9 concepts) make the difference operation free.
* `expected - actual` is exactly the list of problems to report.

---

### 4. Report, Don't Crash

```python
if missing:
    failed += len(missing)
    print("⚠️ Some bookings did not stick — check the log above.")
else:
    print("✅ All bookings verified on the My Bookings page.")
```

---

### 5. Fold It Into the Script

```text
login → book → verify → summary
```

The summary now shows *verified* bookings, not just clicked buttons — the number that
actually means something.

> **Tip:** Verification is also your regression test: change the booking logic, rerun, and
> the verified count tells you instantly whether you broke anything.

---

### Summary Checklist

1. Nav to the bookings page and scrape what the site *says* is booked.
2. Compare against the set of dates the bot intended to book.
3. Report `missing` and `extra` differences explicitly.
4. Count verified bookings in the final summary.
