Here is a structured breakdown of the Day 39 goals — Flight Deal Finder, Part 1.

---

### 1. Skills Covered on Day 39

* **Flight search APIs** (SerpAPI/Google Flights in the current iteration) — searching
  flights with origin, destination and dates
* **Reading rows via Sheety** (GET this time, not POST)
* Parsing deeply nested flight JSON
* Notifications via Twilio SMS

---

### 2. The Project (Part 1)

A Google Sheet lists cities, IATA codes and your target price:

| City | IATA Code | Lowest Price |
|------|-----------|--------------|
| Paris | CDG | 55000 |

The program:

1. GETs every destination from the sheet.
2. Searches flights from your home airport to each city (2–6 months out).
3. If a flight is **cheaper than your target** → SMS you the details.

Part 2 (Day 40) adds user sign-up and emailing everyone.

---

### Summary Checklist

1. Capstone = every API skill since Day 32 in one program.
2. Data-driven: edit the sheet, the app follows.
