import os

LOGO = r"""
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
"""


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def find_highest_bidder(bidding_record):
    """Return (name, amount) of the highest bid in the dictionary."""
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    return winner, highest_bid


bids = {}
bidding_finished = False

print(LOGO)
print("Welcome to the Secret Auction Program")

while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))
    bids[name] = price

    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if should_continue == "yes":
        clear_screen()
    else:
        bidding_finished = True

winner, amount = find_highest_bidder(bids)
print(f"The winner is {winner} with a bid of ${amount}.")
