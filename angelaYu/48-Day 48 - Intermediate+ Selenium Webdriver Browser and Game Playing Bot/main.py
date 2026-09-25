"""
Day 48 Project: Cookie Clicker Bot (Selenium WebDriver).

Plays Cookie Clicker for you: clicks the giant cookie continuously and, every
five seconds, buys the most expensive upgrade it can afford — the one that
raises cookies-per-second the most. After RUN_SECONDS it prints the final
cookies-per-second (CPS) score and quits.

Setup:  pip install selenium
Note:   the classic game page lives at
        https://orteil.dashnet.org/experiments/cookie/
"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

GAME_URL = "https://orteil.dashnet.org/experiments/cookie/"
RUN_SECONDS = 5 * 60          # how long the bot plays for
BUY_INTERVAL = 5              # seconds between shopping trips

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(GAME_URL)

cookie = driver.find_element(By.ID, "bigCookie")

# Shop items are #product0 (cheapest) upward; prices live in #productPrice0 ...
product_ids = [
    element.get_attribute("id")
    for element in driver.find_elements(By.CSS_SELECTOR, "[id^='product']")
]


def current_cookies() -> int:
    """'1,234 cookies' -> 1234"""
    text = driver.find_element(By.ID, "cookies").text
    digits = "".join(ch for ch in text.split(" ")[0] if ch.isdigit())
    return int(digits or 0)


def buy_best_upgrade() -> None:
    """Buy the most expensive upgrade we can afford, or nothing at all."""
    cookies = current_cookies()

    # Most expensive first, so we always grab the biggest CPS boost.
    for product_id in reversed(product_ids):
        index = product_id.replace("product", "")
        price_element = driver.find_element(By.ID, f"productPrice{index}")
        if not price_element.text.strip().isdigit():
            continue
        if cookies >= int(price_element.text):
            try:
                driver.find_element(By.ID, product_id).click()
                print(f"Bought {product_id} for {price_element.text} cookies")
            except Exception:
                pass  # upgrade locked or vanished mid-loop — ignore it
            return


deadline = time.time() + RUN_SECONDS
next_shopping_trip = time.time() + BUY_INTERVAL

while True:
    cookie.click()

    if time.time() > next_shopping_trip:
        buy_best_upgrade()
        next_shopping_trip = time.time() + BUY_INTERVAL

    if time.time() > deadline:
        cps = driver.find_element(By.ID, "cps").text
        print(f"Time's up! Cookies per second: {cps}")
        driver.quit()
        break
