"""
Day 49 Project: Gym class booking bot ("Snack & Lift").

Logs into the course's browser-only gym app with Selenium and books the next
Tuesday and Thursday classes, skipping anything already booked, joining
waitlists when a class is full, then verifies the result on the My Bookings
page and prints a summary.

Setup:
    pip install selenium
    Close Chrome, then set CHROME_PROFILE to the profile folder you use for
    the gym site (the site stores its data in that profile's IndexedDB), and
    GYM_URL to the test site from the course resources.

Only run this against the course's practice site - it is built for testing.
"""

import time
from datetime import date, datetime, timedelta
from functools import wraps

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

GYM_URL = "https://appbrewery.github.io/gym/"          # course practice site
CHROME_PROFILE = ""                                    # e.g. r"C:\ChromeBotProfile"
EMAIL = "student@test.com"
PASSWORD = "password123"

TARGET_WEEKDAYS = {1: "Tuesday", 3: "Thursday"}        # date.weekday(): Mon=0
WEEKS_AHEAD = 4


# --------------------------------------------------------------------------
# Resilience: retry transient failures (network simulation loves these)
# --------------------------------------------------------------------------
def retry(times: int = 3, delay: float = 1.0):
    """Decorator: retry the wrapped function on failure."""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_error = None
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as error:              # noqa: BLE001
                    last_error = error
                    print(f"  ! {func.__name__} attempt {attempt}/{times} failed: {error}")
                    time.sleep(delay * attempt)          # backoff
            raise last_error

        return wrapper

    return decorator


def make_driver() -> webdriver.Chrome:
    options = webdriver.ChromeOptions()
    if CHROME_PROFILE:
        options.add_argument(f"--user-data-dir={CHROME_PROFILE}")
    options.add_experimental_option("detach", False)
    return webdriver.Chrome(options=options)


@retry()
def login(driver) -> None:
    driver.get(f"{GYM_URL}login")
    driver.find_element(By.NAME, "email").send_keys(EMAIL)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))
    print("Logged in.")


def upcoming_dates(weekdays: dict[int, str], weeks: int = WEEKS_AHEAD) -> list[date]:
    """Next `weeks` occurrences of each weekday, ignoring today."""
    today = datetime.now().date()
    dates = []
    for offset in range(weeks * 7):
        day = today + timedelta(days=offset)
        if offset and day.weekday() in weekdays:
            dates.append(day)
    return dates


def booking_state(card) -> str:
    """'booked' | 'waitlist' | 'available' based on the card's button label."""
    label = card.find_element(By.CSS_SELECTOR, "button").text.strip().lower()
    if "booked" in label:
        return "booked"
    if "wait" in label or "full" in label:
        return "waitlist"
    return "available"


@retry()
def book_class(driver, target: date) -> str:
    """Book (or waitlist) the class on `target`; returns the outcome."""
    driver.get(f"{GYM_URL}schedule")
    for card in driver.find_elements(By.CSS_SELECTOR, "div.class-card"):
        heading = card.find_element(By.CSS_SELECTOR, "h3")
        if str(target) not in heading.text and str(target) != heading.get_attribute("data-date"):
            continue

        state = booking_state(card)
        if state == "available":
            card.find_element(By.CSS_SELECTOR, "button").click()
        elif state == "waitlist":
            card.find_element(By.CSS_SELECTOR, "button").click()
        else:
            return "skipped"
        return state
    return "not-found"


def verify_bookings(driver, expected: set[str]) -> set[str]:
    """Dates listed on the My Bookings page."""
    driver.get(f"{GYM_URL}my-bookings")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.booking-row"))
    )
    actual = set()
    for row in driver.find_elements(By.CSS_SELECTOR, "div.booking-row"):
        actual.add(row.find_element(By.CSS_SELECTOR, ".booking-date").text.strip())
    return actual


def main() -> None:
    driver = make_driver()
    counts = {"booked": 0, "waitlist": 0, "skipped": 0, "failed": 0}
    expected = set()

    try:
        login(driver)

        for target in upcoming_dates(TARGET_WEEKDAYS):
            try:
                outcome = book_class(driver, target)
            except Exception as error:                  # noqa: BLE001
                counts["failed"] += 1
                print(f"  x Giving up on {target}: {error}")
                continue

            counts[outcome if outcome in counts else "failed"] += 1
            if outcome in ("available",):
                expected.add(str(target))
            print(f"{TARGET_WEEKDAYS[target.weekday()]} {target}: {outcome}")

        actual = verify_bookings(driver, expected)
        missing = expected - actual

        print("\n" + "=" * 36)
        print("  Snack & Lift booking summary")
        print("=" * 36)
        print(f"  Booked          : {counts['booked']}")
        print(f"  Joined waitlist : {counts['waitlist']}")
        print(f"  Already booked  : {counts['skipped']}")
        print(f"  Failed          : {counts['failed']}")
        print(f"  Verified        : {len(expected & actual)}/{len(expected)}")
        if missing:
            print(f"  MISSING         : {sorted(missing)}")
        print("=" * 36)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
