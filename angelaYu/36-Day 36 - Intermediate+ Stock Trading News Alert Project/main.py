"""Day 36 project: Stock Trading News Alert.

Chains Alpha Vantage (prices) -> NewsAPI (context) -> Twilio (delivery).
Set ALPHAVANTAGE_API_KEY, NEWS_API_KEY, TWILIO_SID, TWILIO_AUTH_TOKEN env vars.
"""

import os

import requests

from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

api_key = os.environ.get("ALPHAVANTAGE_API_KEY")
news_api_key = os.environ.get("NEWS_API_KEY")
twilio_sid = os.environ.get("TWILIO_SID")
twilio_token = os.environ.get("TWILIO_AUTH_TOKEN")

# ---------- STEP 1: stock price movement ----------
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": api_key,
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]

data_list = [value for (key, value) in data.items()]
yesterday_closing = float(data_list[0]["4. close"])
dby_closing = float(data_list[1]["4. close"])

difference = yesterday_closing - dby_closing
up_down = "🔺" if difference > 0 else "🔻"
diff_percent = round((difference / dby_closing) * 100, 2)

# ---------- STEP 2 + 3: news and alerts on a significant move ----------
if abs(diff_percent) > 1:
    news_params = {
        "apiKey": news_api_key,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    articles = news_response.json()["articles"][:3]

    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{diff_percent}%\n"
        f"Headline: {article['title']}.\n"
        f"Brief: {article['description']}"
        for article in articles
    ]

    client = Client(twilio_sid, twilio_token)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=os.environ.get("TWILIO_FROM", "+1234567890"),
            to=os.environ.get("TWILIO_TO", "+911234567890"),
        )
        print(message.status)
else:
    print(f"{STOCK_NAME} moved only {diff_percent}% — no alert needed.")
