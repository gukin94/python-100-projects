import requests
import os
from twilio.rest import Client

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("OWM_API_KEY")
account_sid = "ACd81d80d070928fa0841ae40d27f52d3f"
auth_token = os.environ.get("AUTH_TOKEN")

parameters = {"lat": 37.456257,
              "lon": 126.705208,
              "appid": api_key,
              "exclude": "current,minutely,daily"
              }

response = requests.get(OWM_ENDPOINT, params=parameters)
# print(response.status_code)  # 200 means everything is fine
response.raise_for_status()
weather_data = response.json()

weather_code_12hour = [weather_data["hourly"][hour]['weather'][0]['id'] for hour in range(12)]
for condition in weather_code_12hour:
    if condition < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_='+14422532720',
        to='+821066988650'
    )
    print(message.status)
