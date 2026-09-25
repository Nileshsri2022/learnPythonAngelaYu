"""
Day 53 Capstone: Data Entry Job Automation.

Scrapes real-estate listings (address / price / link) with requests +
BeautifulSoup, then uses Selenium to fill and submit a Google Form once
per listing. Responses collect in the form's linked Google Sheet.

Set up:
    1. Create a Google Form with three short-answer fields labelled
       "Address", "Price" and "Link".
    2. Put its share URL in FORM_URL below.
    3. Update the listings URL and CSS selectors for your target site
       (inspect in DevTools — class names go stale).
"""

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

FORM_URL = "https://forms.gle/YOUR-FORM-ID"
LISTINGS_URL = "https://www.samespeaker.com/rentals"   # example listings site
PAGES = 2


def scrape_listings():
    """Return a list of dicts: address, price, link — from all pages."""
    listings = []
    for page in range(1, PAGES + 1):
        response = requests.get(f"{LISTINGS_URL}?page={page}")
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        for card in soup.select(".property-card"):
            address = card.select_one(".property-address").text.strip()
            price_el = card.select_one(".price-reduced")
            price = price_el.text.split("|")[0].strip() if price_el else "n/a"
            link_el = card.select_one(".property-card-link")
            link = link_el["href"] if link_el else LISTINGS_URL
            listings.append({"address": address, "price": price, "link": link})
    print(f"Scraped {len(listings)} listings.")
    return listings


def submit_to_form(driver, entry):
    driver.get(FORM_URL)
    driver.find_element(
        By.CSS_SELECTOR, "input[aria-label='Address']").send_keys(entry["address"])
    driver.find_element(
        By.CSS_SELECTOR, "input[aria-label='Price']").send_keys(entry["price"])
    driver.find_element(
        By.CSS_SELECTOR, "input[aria-label='Link']").send_keys(entry["link"])
    driver.find_element(By.XPATH, "//span[text()='Submit']").click()
    driver.find_element(
        By.XPATH, "//a[text()='Submit another response']").click()


def main():
    listings = scrape_listings()
    driver = webdriver.Chrome()
    try:
        for entry in listings:
            submit_to_form(driver, entry)
            print(f"Submitted: {entry['address']} ({entry['price']})")
    finally:
        driver.quit()
    print("All listings entered — data entry job automated.")


if __name__ == "__main__":
    main()
