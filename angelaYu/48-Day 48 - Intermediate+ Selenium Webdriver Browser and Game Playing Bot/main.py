"""
Day 48 Project: Cookie Clicker game-playing bot.

Selenium opens the Cookie Clicker game and plays it: every 5 seconds it
reads the cookie count, finds the most expensive affordable upgrade in the
store (list is cheapest-last, so the first affordable hit is the best buy),
buys it, and keeps going for PLAY_MINUTES minutes.

Note: orteil.dashnet.org occasionally updates its markup — if a selector
fails, re-inspect the element in DevTools and update it.
"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

PLAY_MINUTES = 2
CHECK_INTERVAL = 5  # seconds between shop checks

driver = webdriver.Chrome()
try:
    driver.get("https://orteil.dashnet.org/cookieclicker/")

    timeout = time.time() + PLAY_MINUTES * 60
    next_check = time.time() + CHECK_INTERVAL

    while time.time() < timeout:
        if time.time() >= next_check:
            cookie_count = driver.find_element(By.ID, "cookies").text.split()[0]
            cookies = int(cookie_count.replace(",", ""))
            # Cheapest-last so the first affordable item is the best deal.
            items = driver.find_elements(
                By.CSS_SELECTOR, "#store div:not(.toFill)")[::-1]
            for item in items:
                price_text = item.find_element(
                    By.CLASS_NAME, "price").text.replace(",", "")
                if not price_text.isdigit():
                    continue
                if cookies >= int(price_text):
                    item.click()
                    print(f"Bought an upgrade ({price_text} cookies).")
                    break
            next_check = time.time() + CHECK_INTERVAL

    print(driver.find_element(By.ID, "cookiesPerSecond").text)
finally:
    driver.quit()
