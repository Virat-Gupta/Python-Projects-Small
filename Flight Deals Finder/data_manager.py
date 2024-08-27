import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

SHEETY_PRICES_ENDPOINT = f"https://api.sheety.co/{os.environ["SHEETY_PHILL"]}/flightDeals/prices"
SHEETY_USERS_ENDPOINT = f"https://api.sheety.co/{os.environ["SHEETY_PHILL"]}/flightDeals/users"

class DataManager:
    
    def __init__(self) -> None:
        self._user = os.environ["SHEETY_USRERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self._authorization = HTTPBasicAuth(username=self._user,password=self._password)
        self.destination_data = {}
        self.customer_data = {}
    
    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, auth=self._authorization)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data
    
    def update_destination_data(self):
        for city in self.destination_data :
            new_data = {
                "price" : {
                    "iataCode" : city["iataCode"]
                }
            }

            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city["id"]}",
                auth=self._authorization,
                json=new_data
            )
    
    def get_customer_emails(self) :
        response = requests.get(url=SHEETY_USERS_ENDPOINT, auth=self._authorization)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data

# from pprint import pprint
# pprint(DataManager().get_customer_emails()[0]["whatIsYourEmail ?"])