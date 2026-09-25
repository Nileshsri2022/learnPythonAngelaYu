"""
Day 49 Project: Automated gym class booking bot.

Selenium drives the gym website to book the upcoming Tuesday and Thursday
spin classes: navigates, logs in if needed, books each target class,
verifies the "My Bookings" page and prints a run summary. Retries ride out
transient network failures.

Credentials come from environment variables: GYM_EMAIL / GYM_PASSWORD.
Selectors are written against the course's example gym site — update them
from DevTools if your gym's markup differs.
"""

import datetime as dt
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Tuesday=1, Thursday=3 (Monday=0). Add more weekday numbers to book more.
TARGET_WEEKDAYS = [1, 3]
RETRY_ATTEMPTS = 3


def get_today(fake=None):
    """Injectable 'today' so the date logic can be QA'd time-travel style."""
    return fake or dt.datetime.now()


def days_until(weekday_number, today):
    delta = (weekday_number - today.weekday()) % 7
    return delta if delta != 0 else 7


def book_class_on(driver, target_date):
    """Find the class card matching target_date and click Book if possible.

    Returns "booked", "skipped" (already booked) or "failed".
    """
    date_label = target_date.strftime("%d/%m/%Y")
    try:
        cards = driver.find_elements(By.CLASS_NAME, "class-card")
        for card in cards:
            if date_label not in card.text:
                continue
            button = card.find_element(By.TAG_NAME, "button")
            if button.text.strip().lower() == "book":
                button.click()
                return "booked"
            return "skipped"
        return "failed"
    except Exception as error:
        print(f"  Error booking {date_label}: {error}")
        return "failed"


def main():
    driver = webdriver.Chrome()
    booked = skipped = failed = 0
    try:
        driver.get("https://www.gym-site.com/schedule")

        # Login if the form is present (profile cookies usually skip this).
        if driver.find_elements(By.ID, "email"):
            driver.find_element(By.ID, "email").send_keys(
                os.environ.get("GYM_EMAIL"))
            driver.find_element(By.ID, "password").send_keys(
                os.environ.get("GYM_PASSWORD"))
            driver.find_element(
                By.CSS_SELECTOR, "button[type='submit']").click()

        today = get_today()
        for weekday_number in TARGET_WEEKDAYS:
            target = today + dt.timedelta(
                days=days_until(weekday_number, today))
            print(f"Booking class for {target.strftime('%d/%m/%Y')}...")
            for attempt in range(RETRY_ATTEMPTS):
                outcome = book_class_on(driver, target)
                if outcome != "failed":
                    break
                time.sleep(5)
            if outcome == "booked":
                booked += 1
            elif outcome == "skipped":
                skipped += 1
            else:
                failed += 1

        # Verify on the My Bookings page.
        driver.get("https://www.gym-site.com/my-bookings")
        page_text = driver.find_element(By.TAG_NAME, "body").text
        for weekday_number in TARGET_WEEKDAYS:
            target = today + dt.timedelta(
                days=days_until(weekday_number, today))
            if target.strftime("%d/%m/%Y") in page_text:
                print(f"{target.strftime('%d/%m/%Y')} confirmed ✅")
            else:
                print(f"{target.strftime('%d/%m/%Y')} missing ❌")

        print(f"Booked: {booked} | Already booked: {skipped} | Failed: {failed}")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
