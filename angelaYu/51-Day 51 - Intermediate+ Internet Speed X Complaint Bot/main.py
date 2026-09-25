"""
Day 51 Project: Internet Speed Complaint Bot.

Measures your connection on Speedtest with Selenium, compares the result with
the speeds your ISP promised, and (only if they're short) tweets a complaint
at the provider with the numbers.

Setup:
    pip install selenium
    Set X_EMAIL / X_PASSWORD in the environment, review PROMISED_DOWN,
    PROMISED_UP and PROVIDER_HANDLE, then run.

Practise against the course's clone of X; automating a live account can hit
rate limits or a login challenge - log in by hand once, then reuse the profile.
"""

import os
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

SPEEDTEST_URL = "https://www.speedtest.net/"
X_URL = "https://x.com/login"

PROMISED_DOWN = 150          # Mbps from your contract
PROMISED_UP = 10
PROVIDER_HANDLE = "@YourProvider"

X_EMAIL = os.environ.get("X_EMAIL", "")
X_PASSWORD = os.environ.get("X_PASSWORD", "")
PROFILE_DIR = ""             # optional: r"C:\ChromeBotProfile"


def click_if_present(driver, by, value, timeout=5) -> bool:
    try:
        WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((by, value))
        ).click()
        return True
    except TimeoutException:
        return False


class InternetSpeedTwitterBot:
    """Owns the browser, the measured speeds, and the complaint."""

    def __init__(self, promised_down, promised_up):
        self.promised_down = promised_down
        self.promised_up = promised_up
        self.down = 0
        self.up = 0

        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        if PROFILE_DIR:
            options.add_argument(f"--user-data-dir={PROFILE_DIR}")
        self.driver = webdriver.Chrome(options=options)

    # ------------------------------------------------------------------
    def get_internet_speed(self) -> None:
        """Run a Speedtest and store the results on self.down / self.up."""
        self.driver.get(SPEEDTEST_URL)

        click_if_present(self.driver, By.ID, "onetrust-accept-btn-handler")

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "start-text"))
        ).click()

        # a full test can take up to ~2 minutes
        WebDriverWait(self.driver, 180).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.result-container-speed"))
        )

        self.down = float(self.driver.find_element(
            By.CSS_SELECTOR, "span.download-speed").text)
        self.up = float(self.driver.find_element(
            By.CSS_SELECTOR, "span.upload-speed").text)

        print(f"Measured: {self.down} Mbps down / {self.up} Mbps up")

    # ------------------------------------------------------------------
    def tweet_at_provider(self) -> None:
        """Log in to X and post the complaint."""
        self.driver.get(X_URL)

        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.NAME, "text"))
        ).send_keys(X_EMAIL)
        self.driver.find_element(By.XPATH, "//span[text()='Next']").click()

        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.NAME, "password"))
        ).send_keys(X_PASSWORD)
        self.driver.find_element(
            By.CSS_SELECTOR, "button[data-testid='LoginForm_Login_Button']").click()

        message = (
            f"Hey {PROVIDER_HANDLE}, why is my internet speed "
            f"{self.down}down/{self.up}up when I pay for "
            f"{self.promised_down}down/{self.promised_up}up?"
        )

        tweet_box = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-testid='tweetTextarea_0']"))
        )
        tweet_box.click()
        ActionChains(self.driver).send_keys(message).perform()

        self.driver.find_element(
            By.CSS_SELECTOR, "button[data-testid='tweetButtonInline']").click()
        print("Complaint posted:", message)

    # ------------------------------------------------------------------
    def close(self) -> None:
        self.driver.quit()


if __name__ == "__main__":
    bot = InternetSpeedTwitterBot(PROMISED_DOWN, PROMISED_UP)
    try:
        bot.get_internet_speed()
        if bot.down < bot.promised_down or bot.up < bot.promised_up:
            bot.tweet_at_provider()
        else:
            print("Speeds are fine today - no complaint needed.")
    finally:
        bot.close()
