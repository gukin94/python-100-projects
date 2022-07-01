##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas as pd
import random
import os
import smtplib

PATH = "./letter_templates"
PLACE_HOLDER = '[NAME]'
SMTP_GMAIL = "smtp.gmail.com"
CODE_GMAIL = 587

MY_EMAIL = "gukin.test@gmail.com"
MY_PASSWORD = "password"

# letter_choice = []
# for file in os.listdir(PATH):
#     with open(f"{PATH}/{file}") as txt_file:
#         letter_choice.append(txt_file.read())


def get_info(file):
    global PATH
    with open(f"{PATH}/{file}") as txt_file:
        return txt_file.read()


letter_choice = [get_info(file) for file in os.listdir(PATH)]


# 1. Update the birthdays.csv
birthday_info = pd.read_csv("birthdays.csv")
birthday_info = birthday_info.to_dict(orient='records')


# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
today_month = now.month
today_day = now.day

for person_info in birthday_info:
    the_month = person_info["month"]
    the_day = person_info["day"]
    the_person_name = person_info["name"]
    the_person_email= person_info["email"]

    if the_month == today_month and the_day == today_day:
        # print(f"it matches with {person_info['name']}")

        # 3. If step 2 is true, pick a random letter from letter templates and replace
        # the [NAME] with the person's actual name from birthdays.csv
        chosen_letter = random.choice(letter_choice)
        # print(chosen_letter)
        modified_letter = chosen_letter.replace(PLACE_HOLDER, the_person_name)
        print(modified_letter)

        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP(SMTP_GMAIL, CODE_GMAIL) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs="gukin94@gmail.com",
                                msg=f'Subject: Love you from gukin\n\n{modified_letter}')





