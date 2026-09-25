"""
Day 50 Project: Auto Tinder swiping bot (Selenium drill).

Drives a logged-in Tinder/Tindog session: logs in via the Facebook popup,
dismisses the permission dialogs, then clicks Like in a loop until the
free likes run out.

Credentials come from environment variables: FB_EMAIL / FB_PASSWORD.
Tinder's markup changes constantly and auto-liking breaches its ToS —
run this against a practice clone (e.g. Tindog) or a throwaway account.
"""

import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

LIKES_TO_GIVE = 100

driver = webdriver.Chrome()
try:
    driver.get("https://tinder.com/")

    # --- Login via the Facebook popup window -------------------------------
    login_link = driver.find_element(
        By.XPATH, "//a[contains(@href, 'auth') or text()='Log in']")
    login_link.click()
    time.sleep(2)

    fb_button = driver.find_element(
        By.XPATH, "//span[text()='Login with Facebook']")
    fb_button.click()
    time.sleep(2)                       # wait for the popup window

    base_window = driver.window_handles[0]
    fb_window = driver.window_handles[1]
    driver.switch_to.window(fb_window)

    driver.find_element(By.ID, "email").send_keys(os.environ.get("FB_EMAIL"))
    driver.find_element(By.ID, "pass").send_keys(os.environ.get("FB_PASSWORD"))
    driver.find_element(By.NAME, "login").click()

    driver.switch_to.window(base_window)
    time.sleep(5)                       # wait for the app to load

    # --- Dismiss every permission dialog -----------------------------------
    for _ in range(5):
        try:
            dismiss = driver.find_element(
                By.XPATH, "//button[text()='I accept'] | //button[text()='Not now']")
            dismiss.click()
            time.sleep(1)
        except Exception:
            break                       # no more popups

    # --- Like everything ----------------------------------------------------
    like_button = driver.find_element(
        By.XPATH, "//button[@aria-label='Like']")
    for _ in range(LIKES_TO_GIVE):
        like_button.click()
        time.sleep(1)                   # be gentle with the servers

    print(f"Gave {LIKES_TO_GIVE} likes.")
finally:
    driver.quit()
