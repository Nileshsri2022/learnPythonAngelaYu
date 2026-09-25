Here is a structured breakdown of this lesson on the project requirements.

---

### 1. The Spec

1. Scrape a listings site (e.g. apartments.com filtered to a city) and collect, for
   every listing: **address**, **price**, **link**.
2. Create a Google Form with three short-answer questions: address, price, link.
3. For each listing, open the form with Selenium, fill all three fields, click Submit,
   then "Submit another response".
4. Responses land in a linked Google Sheet — the "database".

---

### 2. Hints

* Listings paginate: scrape all pages before touching the form.
* Map each form field with `find_element(By.NAME, "entry.xxxx")` — the `entry` ids come
  from the form's own markup (inspect each input).
* Keep the Selenium part in a loop over a list of dicts: scrape fully, then enter.

---

### Summary Checklist

1. Scrape (address, price, link) × all pages.
2. Form-fill loop: fill → submit → submit-another.
