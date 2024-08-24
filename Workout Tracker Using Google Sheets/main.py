import requests
from datetime import datetime
import os

NUTRI_APP_ID = os.environ["NUTRI_APP_ID"]
NUTRI_API = os.environ["NUTRI_API_KEY"]

HOST_ENDPOINT = "https://trackapi.nutritionix.com"
EXERCISE_ENDPOINT = f"{HOST_ENDPOINT}/v2/natural/exercise"

SHEETY_PHILL = os.environ["SHEETY_URL_PHILL"]
SHEETY_URL = f"https://api.sheety.co/{SHEETY_PHILL}/workoutTracking/workouts"

SHEETY_AUTH_TOKEN = os.environ["SHEETY_AUTH_TOKEN"]

header = {
    "x-app-id" : NUTRI_APP_ID,
    "x-app-key" : NUTRI_API,
}

query_input = input("What you did ? :")

query_params = {
    "query" : query_input
}

response = requests.post(url=EXERCISE_ENDPOINT, json=query_params, headers=header)

SHEETY_HEADER = {
    "Authorization" : f"Bearer {SHEETY_AUTH_TOKEN}"
}

for exercise in response.json()["exercises"] :
    row_data_sheetly = {
        "workout" : {
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%H:%M:%S"),
            "exercise": exercise["user_input"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheetly_response = requests.post(url=SHEETY_URL, json=row_data_sheetly, headers=SHEETY_HEADER)
    print(sheetly_response.json())