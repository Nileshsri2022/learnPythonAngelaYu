# Day 39 Goals: what you will make by the end of the day

Part 1 of the API capstone: a **cheap flight finder** that hunts deals for you every
day and texts you when one appears.

---

### 1. The Idea

Flight prices swing wildly. Rather than picking a destination and then a date, watch
many destinations over the next six months and pounce when a price drops far below
its normal level — exactly how Angela found New Zealand for £350 (normally ~£800)
and Japan for £250 return (normally ~£500).

Doing that by hand means searching every route, every day. A script doesn't get bored.

---

### 2. How the Program Works

```text
Google Sheet (destinations + price cut-off)
        │  e.g. LON → BER, don't pay more than £150
        ▼
Flight search API  ← search the next 6 months, cheapest first
        ▼
price < cut-off ?
        ▼ yes
Twilio SMS → "Low price alert! Only £41 to fly London → Berlin,
              from 25 Aug to 10 Sep"
```

The live demo in the lecture found a Berlin flight **£1 under** the stored
threshold — proof that the logic only needs to be *slightly* better than the market
to be useful.

---

### 3. The New Skills

| Skill | Where it shows up |
|-------|-------------------|
| **Google Sheets as a database** | The `prices`/`destinations` tab holds the cut-offs |
| **Search API with parameters** | Origin, destination, dates, currency, `max_price` |
| **Reading nested JSON** | `best_flights` / `other_flights` lists inside the response |
| **Sending rich SMS** | Twilio message built from the found deal |

---

### Summary Checklist

1. Flight finder = sheet of destinations + cut-off prices → search API → SMS on a hit.
2. Compare the API's cheapest price with your stored threshold; alert if lower.
3. Store and reconnect real data end-to-end (Sheety/Google Sheets, search API, Twilio).
4. Part 2 turns this personal tool into a product with **users**.
