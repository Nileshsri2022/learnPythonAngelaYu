"""
Day 53 Capstone Project: Data Entry Job Automation.

Scrapes the course's Zillow clone (San Francisco rentals, up to $3,000, one
bedroom) with requests + Beautiful Soup, then types every listing - address,
price and link - into a Google Form with Selenium. The form's Responses tab
can be linked to a Google Sheet, which is the spreadsheet the "client" wants.

Setup:
    pip install requests beautifulsoup4 selenium
    Create a Google Form with three short-answer questions in this order:
        1. Address   2. Price   3. Link
    Paste its viewform URL into FORM_URL below, then run.
"""

import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"
FORM_URL = "https://docs.google.com/forms/d/e/YOUR_FORM_ID/viewform"


def scrape_listings() -> list[tuple[str, str, str]]:
    """Return (address, price, link) for every listing on the page."""
    response = requests.get(ZILLOW_URL, timeout=30)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    links = [a["href"] for a in soup.select("a.property-card-link")]
    prices = [
        clean_price(p.getText())
        for p in soup.select(".PropertyCardWrapper__StyledPriceLine")
    ]
    addresses = [a.getText().strip() for a in soup.select("address")]

    assert len(addresses) == len(prices) == len(links), (
        f"cards out of sync: {len(addresses)} addresses, "
        f"{len(prices)} prices, {len(links)} links"
    )
    return list(zip(addresses, prices, links))


def clean_price(raw: str) -> str:
    """'$2,895/mo' or '$2,895+ 1bd' -> '2895'."""
    return raw.split("/")[0].replace("$", "").replace(",", "").strip()


def submit_to_form(listings: list[tuple[str, str, str]]) -> None:
    """Open the Google Form once per listing and submit the three values."""
    driver = webdriver.Chrome()

    try:
        for index, (address, price, link) in enumerate(listings, start=1):
            driver.get(FORM_URL)

            fields = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")
            fields[0].send_keys(address)
            fields[1].send_keys(price)
            fields[2].send_keys(link)

            driver.find_element(By.XPATH, "//span[text()='Submit']").click()

            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH,
                         "//*[contains(text(), 'Your response has been recorded')]")
                    )
                )
            except TimeoutException:
                print(f"  ! submission {index} not confirmed")

            print(f"  [{index}/{len(listings)}] {price:>6} | {address[:45]}")
            time.sleep(1)          # be polite between submissions
    finally:
        driver.quit()


if __name__ == "__main__":
    listings = scrape_listings()
    print(f"Found {len(listings)} listings on the Zillow clone.")
    submit_to_form(listings)
    print("Done - check the form's Responses tab / linked Google Sheet.")
