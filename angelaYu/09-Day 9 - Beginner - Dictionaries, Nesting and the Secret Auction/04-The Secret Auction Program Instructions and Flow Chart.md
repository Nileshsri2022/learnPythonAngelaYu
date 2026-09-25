# The Secret Auction Program Instructions and Flow Chart

---

### 1. Program Flow

1. Print the logo and greet the bidders.
2. Ask a bidder for their **name** and **bid**.
3. Store them: `bids[name] = amount` (a dictionary grows with every bidder).
4. Ask *"Are there any other bidders? Type 'yes' or 'no'."*
   * `yes` → clear the screen (so nobody sees the previous bid) and go to step 2.
   * `no` → find and announce the **winner**.

The flowchart's loop-back arrow (from Day 7's lesson) is this program's `while` loop.

---

### 2. Finding the Highest Bidder

Two ways — the loop, and the built-in:

```python
# Way 1: loop over the dictionary
highest_bid = 0
winner = ""
for bidder in bids:
    bid_amount = bids[bidder]
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bidder

# Way 2: max() with a key function
winner = max(bids, key=bids.get)
```

---

### 3. Solution

```python
from replit import clear   # on non-Replit environments: import os; os.system('clear')

print(r"""
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
""")

bids = {}
bidding_finished = False

while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True

winner = max(bids, key=bids.get)
print(f"The winner is {winner} with a bid of ${bids[winner]}.")
```

> **Note:** On Replit, `from replit import clear` wipes the console between bidders —
> the secrecy part of the auction. Locally, `os.system('clear')` (or `'cls'` on Windows)
> does the same job.

---

### Summary Checklist

1. Bids accumulate in a **dictionary**: `bids[name] = amount`.
2. A `while` loop drives the rounds until bidding finishes.
3. Highest bid: manual loop or `max(bids, key=bids.get)`.
4. Runnable version: [`blind_auction.py`](blind_auction.py)
