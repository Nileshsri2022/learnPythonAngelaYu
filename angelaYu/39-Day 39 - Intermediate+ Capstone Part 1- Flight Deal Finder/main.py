"""Day 39 capstone part 1: Flight Deal Finder.

Set SHEET_ENDPOINT, SHEET_TOKEN, SERPAPI_KEY, TWILIO_SID, TWILIO_AUTH_TOKEN,
TWILIO_FROM, TWILIO_TO environment variables.
"""

import os

import requests

from twilio.rest import Client

ORIGIN = "DEL"   # your home airport IATA code
FLIGHT_SEARCH_ENDPOINT = "https://serpapi.com/search.json"

data_manager_endpoint = os.environ.get("SHEET_ENDPOINT")
sheet_headers = {"Authorization": f"Bearer {os.environ.get('SHEET_TOKEN')}"}


def get_destinations():
    response = requests.get(url=data_manager_endpoint, headers=sheet_headers)
    response.raise_for_status()
    return response.json()["prices"]


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
    response = requests.get(FLIGHT_SEARCH_ENDPOINT, params=params)
    response.raise_for_status()
    return response.json()


def find_cheapest(data):
    offers = data.get("best_flights") or data.get("other_flights") or []
    cheapest = None
    for offer in offers:
        if cheapest is None or offer["price"] < cheapest["price"]:
            cheapest = offer
    return cheapest


def send_sms(message_body):
    client = Client(os.environ.get("TWILIO_SID"), os.environ.get("TWILIO_AUTH_TOKEN"))
    message = client.messages.create(
        body=message_body,
        from_=os.environ.get("TWILIO_FROM"),
        to=os.environ.get("TWILIO_TO"),
    )
    print(message.status)


for destination in get_destinations():
    city = destination["city"]
    code = destination["iataCode"]
    target = destination["lowestPrice"]

    cheapest = find_cheapest(search_flight(code))
    if cheapest and cheapest["price"] < target:
        first_leg = cheapest["flights"][0]
        send_sms(
            f"Low price alert! Only ₹{cheapest['price']} to fly from {ORIGIN} "
            f"to {code} ({city}), "
            f"out {first_leg['departure_airport']['time'][:10]}."
        )
    else:
        print(f"No deals to {city} right now.")
