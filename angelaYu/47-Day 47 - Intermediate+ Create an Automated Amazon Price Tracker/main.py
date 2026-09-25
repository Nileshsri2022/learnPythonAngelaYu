"""
Day 47 Project: Automated Amazon Price Tracker.

Watches one Amazon product; if its price drops below BUY_PRICE, emails you
a deal alert. Credentials come from environment variables:
    MY_EMAIL / MY_EMAIL_PASSWORD  (Gmail app password)

Set BUY_PRICE and URL below, then run daily (cron / Task Scheduler /
GitHub Actions).
"""

import os
import smtplib

import requests
from bs4 import BeautifulSoup

URL = ("https://www.amazon.com/dp/B075CYNTQV/"
       "ref=sxin_13?asc_contentfield=keyword&keywords=instant+pot")
BUY_PRICE = 100  # your target price in the product's currency

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(URL, headers=header)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")

# Price: first .a-offscreen span; clean "₹12,999.00"/"$129.99" into a float.
price_tag = soup.find(name="span", class_="a-offscreen")
price_text = price_tag.getText()
digits = "".join(ch for ch in price_text if ch.isdigit() or ch == ".")
price = float(digits)

title_tag = soup.find(name="span", id="productTitle")
product_title = title_tag.getText().strip()

if price < BUY_PRICE:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=os.environ.get("MY_EMAIL"),
                         password=os.environ.get("MY_EMAIL_PASSWORD"))
        connection.sendmail(
            from_addr=os.environ.get("MY_EMAIL"),
            to_addrs=os.environ.get("MY_EMAIL"),
            msg=(f"Subject:Amazon Price Alert!\n\n{product_title} is now "
                 f"{price_text}\n{URL}").encode("utf-8"),
        )
    print(f"Alert sent: {product_title} at {price_text}")
else:
    print(f"No alert: {product_title} is {price_text} (target {BUY_PRICE}).")
