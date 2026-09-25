"""
Day 50 Project: Auto Tinder Swiping Bot (Selenium).

Opens the dating app, logs in through the Facebook popup, dismisses the
notification/location/cookie modals a fresh session is greeted with, then
swipes (dislikes by default - flip PREFER_LIKE to True to match instead).

Setup:
    pip install selenium
    Log in once with `--user-data-dir` pointing at a dedicated profile so the
    session (and any captcha you solved by hand) persists for later runs.

Practise against the course's clone site. Running bots against live dating
apps breaks their terms of service and can get accounts suspended.
"""

import os
import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

APP_URL = "https://tinder.com"              # or the course's Tindog clone
PROFILE_DIR = ""                            # e.g. r"C:\ChromeBotProfile"
FB_EMAIL = os.environ.get("FB_EMAIL", "")
FB_PASSWORD = os.environ.get("FB_PASSWORD", "")

SWIPE_LIMIT = 50                            # stay under the ~100/day free cap
PREFER_LIKE = False                         # False = dislike (kinder to humans)


def click_if_present(driver, by, value, timeout=5) -> bool:
    """Click the first match if it shows up within `timeout`; otherwise move on."""
    try:
        WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((by, value))
        ).click()
        return True
    except TimeoutException:
        return False


def build_driver() -> webdriver.Chrome:
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    if PROFILE_DIR:
        options.add_argument(f"--user-data-dir={PROFILE_DIR}")
    options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.geolocation": 1,
        "profile.default_content_setting_values.notifications": 1,
    })
    return webdriver.Chrome(options=options)


def login(driver) -> None:
    """Open the app and log in through the Facebook popup (new window handle)."""
    driver.get(APP_URL)

    click_if_present(driver, By.XPATH, "//button[text()='Log in']", timeout=10)
    click_if_present(driver, By.CSS_SELECTOR, "button[aria-label='Log in with Facebook']", timeout=10)

    windows = driver.window_handles
    if len(windows) > 1:
        driver.switch_to.window(windows[1])
        driver.find_element(By.ID, "email").send_keys(FB_EMAIL)
        driver.find_element(By.ID, "pass").send_keys(FB_PASSWORD)
        driver.find_element(By.NAME, "login").click()
        WebDriverWait(driver, 20).until(EC.url_contains(APP_URL.split("//")[1]))
        driver.switch_to.window(windows[0])


def dismiss_requests(driver) -> None:
    """Click away every optional modal blocking the swipe view."""
    dismissals = [
        (By.XPATH, "//button[text()='Not interested']"),
        (By.XPATH, "//button[text()=\"I'll pass\"]"),
        (By.XPATH, "//button[text()='Allow']"),
        (By.CSS_SELECTOR, "button[aria-label='Dismiss']"),
    ]
    for by, value in dismissals:
        click_if_present(driver, by, value, timeout=3)


def swipe(driver) -> None:
    """Like/dislike profiles until the limit, a match popup, or the end."""
    label = "Like" if PREFER_LIKE else "Nope"
    button = (By.CSS_SELECTOR, f"button[aria-label='{label}']")

    WebDriverWait(driver, 15).until(EC.element_to_be_clickable(button))
    dismiss_requests(driver)

    count = 0
    for _ in range(SWIPE_LIMIT):
        try:
            driver.find_element(*button).click()
            count += 1
        except Exception as error:                       # noqa: BLE001
            print(f"Stopped swiping after {count}: {error}")
            break

        # match popup / promo overlay blocks the next card - clear it
        click_if_present(driver, By.XPATH, "//button[text()='Back to Tinder']", timeout=2)
        click_if_present(driver, By.CSS_SELECTOR, "button[aria-label='Dismiss']", timeout=1)
        time.sleep(1)                                    # polite pacing

    print(f"Swiped {count} profiles this session.")
    driver.quit()


if __name__ == "__main__":
    bot_driver = build_driver()
    login(bot_driver)
    dismiss_requests(bot_driver)
    swipe(bot_driver)
