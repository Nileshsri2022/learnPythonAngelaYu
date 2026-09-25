"""Day 37 project: Pixela habit tracker — POST/PUT/DELETE with header auth.

Set PIXELA_TOKEN and PIXELA_USERNAME environment variables before running.
"""

import os

import requests

from datetime import datetime

TOKEN = os.environ.get("PIXELA_TOKEN", "abc1234567890")
USERNAME = os.environ.get("PIXELA_USERNAME", "yourname")
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
headers = {"X-USER-TOKEN": TOKEN}


def create_user():
    user_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }
    response = requests.post(url=pixela_endpoint, json=user_params)
    print(response.text)


def create_graph():
    graph_config = {
        "id": GRAPH_ID,
        "name": "Coding Graph",
        "unit": "hours",
        "type": "float",
        "color": "ajisai",
    }
    response = requests.post(url=f"{pixela_endpoint}/{USERNAME}/graphs",
                             json=graph_config, headers=headers)
    print(response.text)


def add_pixel(quantity: str):
    today = datetime.now().strftime("%Y%m%d")
    pixel_data = {"date": today, "quantity": quantity}
    response = requests.post(url=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}",
                             json=pixel_data, headers=headers)
    print(response.text)


def update_pixel(quantity: str, date: str | None = None):
    date = date or datetime.now().strftime("%Y%m%d")
    response = requests.put(url=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}",
                            json={"quantity": quantity}, headers=headers)
    print(response.text)


def delete_pixel(date: str):
    response = requests.delete(url=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}",
                               headers=headers)
    print(response.text)


# Run once each, in order:
# create_user()
# create_graph()
add_pixel(input("How many hours did you code today? "))
# update_pixel("8")
# delete_pixel("20260925")
