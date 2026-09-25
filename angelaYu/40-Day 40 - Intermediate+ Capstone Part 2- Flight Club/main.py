"""Day 40 capstone part 2: Flight Club — deals emailed to signed-up users.

Set SHEET_ENDPOINT, SHEET_TOKEN, SERPAPI_KEY, MY_EMAIL, MY_PASSWORD env vars.
The Sheety project needs both `prices` and `users` tabs.
"""

import os

import smtplib

import requests

ORIGIN = "DEL"
SHEET_ENDPOINT = os.environ.get("SHEET_ENDPOINT")
HEADERS = {"Authorization": f"Bearer {os.environ.get('SHEET_TOKEN')}"}


def get_data(tab: str):
    response = requests.get(f"{SHEET_ENDPOINT}/{tab}", headers=HEADERS)
    response.raise_for_status()
    return response.json()[tab]


def search_flight(destination_code: str):
    from datetime import datetime, timedelta

    params = {
        "engine": "google_flights",
        "departure_id": ORIGIN,
        "arrival_id": destination_code,
        "outbound_date": (datetime.now() + timedelta(days=180)).strftime("%Y-%m-%d"),
        "return_date": (datetime.now() + timedelta(days=187)).strftime("%Y-%m-%d"),
        "currency": "INR",
        "hl": "en",
        "api_key": os.environ.get("SERPAPI_KEY"),
    }
    response = requests.get("https://serpapi.com/search.json", params=params)
    response.raise_for_status()
    return response.json()


def find_cheapest(data):
    offers = data.get("best_flights") or data.get("other_flights") or []
    cheapest = None
    for offer in offers:
        if cheapest is None or offer["price"] < cheapest["price"]:
            cheapest = offer
    return cheapest


def send_emails(emails, message_body):
    my_email = os.environ.get("MY_EMAIL")
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=os.environ.get("MY_PASSWORD"))
        for email in emails:
            connection.sendmail(
                from_addr=my_email,
                to_addrs=email,
                msg=f"Subject:New Low Price Flight!\n\n{message_body}",
            )
    print(f"Emailed {len(emails)} customers.")


customer_emails = [user["email"] for user in get_data("users")]

for destination in get_data("prices"):
    cheapest = find_cheapest(search_flight(destination["iataCode"]))
    if cheapest and cheapest["price"] < destination["lowestPrice"]:
        first_leg = cheapest["flights"][0]
        message = (
            f"Only ₹{cheapest['price']} to fly from {ORIGIN} to "
            f"{destination['iataCode']} ({destination['city']}), "
            f"out {first_leg['departure_airport']['time'][:10]}, "
            f"{cheapest.get('type', 'flight')} available!\n"
        )
        send_emails(customer_emails, message)
    else:
        print(f"No deals to {destination['city']} right now.")
