import requests
from twilio.rest import Client
import os

API_KEY = os.environ.get("WEATHER_API_KEY")

account_sid = os.environ.get("TWILIO_ACCOUTN_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

from_phone = os.environ.get("FROM_PH")
to_phone = os.environ.get("TO_PH")

parameters = {
    "lat":51.588470,
    "lon":5.326350,
    "cnt":4,
    "appid":API_KEY
}

response = requests.get(url=r"https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()

carry_umbrealla = False
for lst in response.json()["list"]:
    for weather_type in lst["weather"]:
        if weather_type["id"] <= 700:
            carry_umbrealla = True

if carry_umbrealla :
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="IT GONNA RAIN.",
        from_=from_phone,
        to=to_phone,
    )

# weather_data = response.json()["list"][0]["weather"]
# print(weather_data)