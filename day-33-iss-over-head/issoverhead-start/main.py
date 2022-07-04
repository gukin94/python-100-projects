import requests
from datetime import datetime
import smtplib
import threading
import time

MY_EMAIL = "gukin.test@gmail.com"
MY_PASSWORD = "gyiyxhntftgdenyk"
MY_LAT = 37.456257 # Your latitude
MY_LONG = 126.705208 # Your longitude


def utc_to_kst(utc_hour):
    return (utc_hour+9) % 24


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
hour_now = time_now.hour


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

def my_app():
    threading.Timer(60, my_app).start()
    #time.sleep(60)
    print("check every 60s")
    if is_over_head() and is_night():
        send_email()


def is_night():
    if utc_to_kst(sunset) < hour_now < utc_to_kst(sunrise):
        print("It's dark enough to observe ISS")
        return True


def is_over_head():
    if MY_LAT - 5 < iss_latitude < MY_LAT + 5 and MY_LONG - 5 < iss_longitude < MY_LONG + 5:
        print("ISS is close to your position")
        return True


def send_email():
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="gukin94@gmail.com",
                            msg="Subject:Hey gukin\n\nLook up!")


my_app()
