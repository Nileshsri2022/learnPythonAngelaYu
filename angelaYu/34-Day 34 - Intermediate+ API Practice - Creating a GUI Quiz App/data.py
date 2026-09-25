import html

import requests

parameters = {
    "amount": 10,
    "type": "boolean",
}


def fetch_questions() -> list:
    response = requests.get("https://opentdb.com/api.php", params=parameters)
    response.raise_for_status()
    data = response.json()
    return data["results"]


question_data = fetch_questions()
