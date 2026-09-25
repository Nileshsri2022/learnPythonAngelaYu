"""
Day 52 Project: Instagram follower bot (Selenium drill).

Logs into Instagram (or a practice clone), opens a target account's
followers modal, scrolls until enough followers are loaded, then visits
each profile and clicks Follow (skipping ones already followed).

Credentials come from environment variables: IG_USERNAME / IG_PASSWORD.
Mass-following breaches Instagram's ToS and its bot-detection is aggressive
— prefer a practice clone / throwaway account, and keep the pacing slow.
"""

import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

TARGET_ACCOUNT = "chefsteps"
TARGET_FOLLOWER_COUNT = 50
PACING_SECONDS = 2


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        driver = self.driver
        # Dismiss the cookie banner if it appears.
        try:
            driver.find_element(
                By.XPATH, "//button[text()='Allow essential cookies']").click()
        except Exception:
            pass
        driver.find_element(By.NAME, "username").send_keys(self.username)
        driver.find_element(By.NAME, "password").send_keys(self.password)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(5)

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{TARGET_ACCOUNT}/")
        time.sleep(3)
        self.driver.find_element(
            By.PARTIAL_LINK_TEXT, "followers").click()
        time.sleep(2)

        modal = self.driver.find_element(By.CLASS_NAME, "isgrP")
        while True:
            self.driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)
            elements = self.driver.find_elements(By.CLASS_NAME, "FPmhX")
            if len(elements) >= TARGET_FOLLOWER_COUNT:
                break
        return [el.get_attribute("title") for el in elements]

    def follow_all(self, usernames):
        for username in usernames:
            self.driver.get(f"https://www.instagram.com/{username}/")
            time.sleep(PACING_SECONDS)
            try:
                button = self.driver.find_element(
                    By.CSS_SELECTOR, "button button")
                if button.text == "Follow":
                    button.click()
                    print(f"Followed {username}.")
                else:
                    print(f"Already following {username}.")
            except Exception as error:
                print(f"Skipped {username}: {error}")
            time.sleep(PACING_SECONDS)

    def run(self):
        try:
            self.login()
            usernames = self.find_followers()
            self.follow_all(usernames)
        finally:
            self.driver.quit()


if __name__ == "__main__":
    InstagramBot(
        os.environ.get("IG_USERNAME"),
        os.environ.get("IG_PASSWORD"),
    ).run()
