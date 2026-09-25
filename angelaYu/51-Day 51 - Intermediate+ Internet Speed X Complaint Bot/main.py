"""
Day 51 Project: Internet Speed X (Twitter) Complaint Bot.

Measures your real download/upload speed and, if it falls short of what
your ISP promises, logs into X and posts a complaint tweet tagging the
provider.

Credentials come from environment variables:
    X_EMAIL / X_PASSWORD  (and X_USERNAME if X asks for the handle first)

Selectors are written against x.com's current markup (data-testid
attributes are the most stable) — verify from DevTools before running.
"""

import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

PROMISED_DOWN = 150   # Mbps your ISP advertises
PROMISED_UP = 20
PROVIDER_HANDLE = "YourISP"


class InternetSpeedTwitterBot:
    def __init__(self, promised_down, promised_up):
        self.promised_down = promised_down
        self.promised_up = promised_up
        self.down = 0.0
        self.up = 0.0
        self.driver = webdriver.Chrome()

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.find_element(By.CSS_SELECTOR, ".js-start-test").click()
        time.sleep(45)  # the speed test genuinely takes ~30-60s
        self.down = float(self.driver.find_element(
            By.CLASS_NAME, "download-value").text)
        self.up = float(self.driver.find_element(
            By.CLASS_NAME, "upload-value").text)
        print(f"Measured: {self.down} Mbps down / {self.up} Mbps up")

    def tweet_at_provider(self):
        self.driver.get("https://x.com/login")
        time.sleep(3)
        driver = self.driver

        driver.find_element(
            By.CSS_SELECTOR, "input[autocomplete='username']").send_keys(
            os.environ.get("X_EMAIL"))
        driver.find_elements(
            By.CSS_SELECTOR, "div[role='button']")[-2].click()
        time.sleep(2)
        driver.find_element(
            By.CSS_SELECTOR, "input[type='password']").send_keys(
            os.environ.get("X_PASSWORD"))
        driver.find_elements(
            By.CSS_SELECTOR, "div[role='button']")[-1].click()
        time.sleep(5)

        tweet_box = driver.find_element(
            By.CSS_SELECTOR, "div[data-testid='tweetTextarea_0']")
        tweet_box.send_keys(
            f"Hey @{PROVIDER_HANDLE}, why is my internet speed "
            f"{self.down}Mbps down/{self.up}Mbps up when I pay for "
            f"{self.promised_down}Mbps down/{self.promised_up}Mbps up?")
        driver.find_element(
            By.CSS_SELECTOR, "div[data-testid='tweetButtonInline']").click()
        print("Complaint posted.")

    def run(self):
        try:
            self.get_internet_speed()
            if self.down < self.promised_down or self.up < self.promised_up:
                self.tweet_at_provider()
            else:
                print("Speeds are fine — no complaint today.")
        finally:
            self.driver.quit()


if __name__ == "__main__":
    bot = InternetSpeedTwitterBot(PROMISED_DOWN, PROMISED_UP)
    bot.run()
