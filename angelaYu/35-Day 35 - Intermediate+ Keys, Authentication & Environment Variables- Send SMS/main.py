"""Day 35 project: Rain Alert — OpenWeatherMap forecast + Twilio SMS/WhatsApp.

Set these environment variables before running:
  OWM_API_KEY, TWILIO_SID, TWILIO_AUTH_TOKEN
"""

import os

import requests

from twilio.rest import Client

OMW_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
MY_LAT = 26.8467
MY_LONG = 80.9462

api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("TWILIO_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "units": "metric",
    "cnt": 12,
}

response = requests.get(OMW_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = int(hour_data["weather"][0]["id"])
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella ☔",
        from_=os.environ.get("TWILIO_FROM", "whatsapp:+14155238886"),
        to=os.environ.get("TWILIO_TO", "whatsapp:+911234567890"),
    )
    print(message.status)
else:
    print("No rain expected in the next 12 hours.")
