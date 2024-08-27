import os
import requests
from dotenv import load_dotenv

load_dotenv()

IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        self._api_key = os.environ["AMADEUS_API_KEY"]
        self._api_secret = os.environ["AMADEUS_API_SECRET"]
        self._token = self._get_new_token()

    def _get_new_token(self) -> str:
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }

        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)
        # print(response.json())
        print(f"Your token is {response.json()['access_token']}")
        print(f"Your token expires in {response.json()['expires_in']} seconds")
        return response.json()["access_token"]


    def get_IATA_code(self, city_name : str) -> str:
        headers = {
            "Authorization": f"Bearer {self._token}"
        }
        query = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS",
        }

        response = requests.get(
            url=IATA_ENDPOINT,
            headers=headers,
            params=query
        )

        print(f"Status Code {response.status_code}.\nAirport IATA: {response.text}")

        try:
            code = response.json()["data"][0]["iataCode"]
        except IndexError:
            print(f"indexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "N/A"
        return code


    def get_flights_to(self, IATA_CODE, from_time, to_time, is_direct=True):

        headers = {
            "Authorization": f"Bearer {self._token}"
        }
        
        query = {
            "originLocationCode" : "LON",
            "destinationLocationCode" : IATA_CODE,
            "departureDate" : from_time.strftime("%Y-%m-%d"),
            "returnDate" : to_time.strftime("%Y-%m-%d"),
            "adults" : 1,
            "nonStop" : "true" if is_direct else "false",
            "currencyCode" : "GBP",
            "max" : 10,
        }

        response = requests.get(
            url=FLIGHT_ENDPOINT,
            headers=headers,
            params=query
        )

        if response.status_code != 200 :
            print("ERROR FETCHING FLIGHT DATA")
            print(response.text)
            return None
    
        return response.json()