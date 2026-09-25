"""Day 32 project: Automated Birthday Wisher.

Requires: birthdays.csv, letter_templates/letter_1..3.txt, SMTP credentials.
"""

import datetime as dt
import os
import random

import pandas as pd

import smtplib

my_email = os.environ.get("MY_EMAIL", "your@gmail.com")
password = os.environ.get("MY_PASSWORD", "app_password")

today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pd.read_csv("birthdays.csv")

# Dictionary comprehension over the rows: (month, day) -> row
birthdays_dict = {(data_row["month"], data_row["day"]): data_row
                  for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"

    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}",
        )
    print(f"Birthday email sent to {birthday_person['name']}")
else:
    print("No birthdays today.")
