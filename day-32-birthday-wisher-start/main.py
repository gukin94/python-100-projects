import random
import datetime as dt
import smtplib

MY_EMAIL = "gukin.test@gmail.com"
MY_PASSWORD = "password"

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 3:

    with open("quotes.txt") as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)

    print(quote)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user= MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="gukin94@gmail.com",
            msg=f"Subject: Hello\n\n{quote}"
        )




