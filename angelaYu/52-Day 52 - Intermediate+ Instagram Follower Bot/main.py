"""
Day 52 Project: Instagram Follower Bot.

Logs in to Instagram (or the course's "Share-a-Naan" clone), opens a similar
account, then follows the people in its followers list - many of whom follow
a food/tech/whatever brand back.

Setup:
    pip install selenium
    Set INSTA_USERNAME / INSTA_PASSWORD in the environment and pick
    SIMILAR_ACCOUNT. Use a dedicated Chrome profile so the login persists.

Keep FOLLOW_LIMIT small (10-20 per run): Instagram rate-limits automated
following and will temporarily block the account if you push too hard.
"""

import os
import random
import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

BASE_URL = "https://www.instagram.com"       # or the Share-a-Naan clone URL
SIMILAR_ACCOUNT = "chefsteps"                # audience you want to tap into
INSTA_USERNAME = os.environ.get("INSTA_USERNAME", "")
INSTA_PASSWORD = os.environ.get("INSTA_PASSWORD", "")
PROFILE_DIR = ""                             # optional: r"C:\ChromeBotProfile"

FOLLOW_LIMIT = 20                            # per run - keep it human-sized
SCROLLS = 5


def click_if_present(driver, by, value, timeout=5) -> bool:
    try:
        WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((by, value))
        ).click()
        return True
    except TimeoutException:
        return False


class InstaFollower:
    """Log in, open the target account's followers modal, follow a few people."""

    def __init__(self, similar_account: str, username: str, password: str, debug=False):
        self.similar_account = similar_account
        self.username = username
        self.password = password
        self.debug = debug            # True -> skip the following step

        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        if PROFILE_DIR:
            options.add_argument(f"--user-data-dir={PROFILE_DIR}")
        self.driver = webdriver.Chrome(options=options)

    # ------------------------------------------------------------------
    def login(self) -> None:
        self.driver.get(BASE_URL)

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "username"))
        ).send_keys(self.username)
        self.driver.find_element(By.NAME, "password").send_keys(self.password)
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # post-login popups: "Save your login info?" / "Turn on notifications?"
        click_if_present(self.driver, By.XPATH, "//button[text()='Not now']")
        click_if_present(self.driver, By.XPATH, "//button[text()='Not Now']")
        print("Logged in.")

    # ------------------------------------------------------------------
    def find_followers(self) -> None:
        self.driver.get(f"{BASE_URL}/{self.similar_account}/")

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "followers"))
        ).click()

        dialog = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='dialog']"))
        )

        # the followers list is an infinite-scrolling modal, not a page
        for _ in range(SCROLLS):
            self.driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight", dialog
            )
            time.sleep(2)

        if "try again later" in dialog.text.lower():
            print("Rate limited while loading followers - stopping.")
            return

        print("Followers list loaded.")

    # ------------------------------------------------------------------
    def follow(self, limit: int = FOLLOW_LIMIT) -> None:
        if self.debug:
            print("DEBUG mode - not following anyone.")
            return

        dialog = self.driver.find_element(By.CSS_SELECTOR, "div[role='dialog']")
        followed = 0

        for button in dialog.find_elements(By.CSS_SELECTOR, "button"):
            if button.text != "Follow":          # skip "Following"/"Requested"
                continue
            try:
                button.click()
                followed += 1
            except Exception as error:           # noqa: BLE001
                print(f"Stopped at {followed}: {error}")
                break

            time.sleep(random.uniform(2, 5))     # human-ish pacing

            if followed >= limit:
                break

        print(f"Followed {followed} accounts.")

    # ------------------------------------------------------------------
    def close(self) -> None:
        self.driver.quit()


if __name__ == "__main__":
    bot = InstaFollower(SIMILAR_ACCOUNT, INSTA_USERNAME, INSTA_PASSWORD)
    try:
        bot.login()
        bot.find_followers()
        bot.follow()
    finally:
        bot.close()
