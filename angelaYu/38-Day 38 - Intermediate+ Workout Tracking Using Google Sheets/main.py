"""Day 38 project: Workout Tracker — natural language in, Google Sheet rows out.

Set NIX_APP_ID, NIX_API_KEY, SHEET_TOKEN and SHEET_ENDPOINT env vars.
SHEET_ENDPOINT looks like: https://api.sheety.co/<user>/myWorkouts/workouts
"""

import os

import requests

from datetime import datetime

NIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

APP_ID = os.environ.get("NIX_APP_ID")
API_KEY = os.environ.get("NIX_API_KEY")
SHEET_TOKEN = os.environ.get("SHEET_TOKEN")
SHEET_ENDPOINT = os.environ.get("SHEET_ENDPOINT")

nix_headers = {"x-app-id": APP_ID, "x-app-key": API_KEY}
sheet_headers = {"Authorization": f"Bearer {SHEET_TOKEN}"}

# ---------- 1. Ask and parse ----------
exercise_text = input("Tell me which exercises you did: ")

parameters = {
    "query": exercise_text,
    "gender": "male",
    "weight_kg": 72.5,
    "height_cm": 172.5,
    "age": 30,
}
response = requests.post(NIX_ENDPOINT, json=parameters, headers=nix_headers)
response.raise_for_status()
result = response.json()

# ---------- 2. Post each exercise to the sheet ----------
today = datetime.now()

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    sheet_response = requests.post(SHEET_ENDPOINT, json=sheet_inputs,
                                   headers=sheet_headers)
    print(sheet_response.text)
