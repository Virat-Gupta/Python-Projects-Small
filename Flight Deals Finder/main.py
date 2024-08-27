#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import time
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()

ORIGIN_CITY_DATA = "LON"

for city_data in sheet_data:
    if city_data["iataCode"] == "":
        from flight_search import FlightSearch
        fligt_search = FlightSearch()
        city_data["iataCode"] = fligt_search.get_IATA_code(city_data["city"])


data_manager.destination_data = sheet_data
data_manager.update_destination_data()

#Retrieve Customer Emails
customer_data = data_manager.get_customer_emails()
customer_email_list = [row["whatIsYourEmail ?"] for row in customer_data]

# Seach for Flights DIrect
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6*30))

notification_manager = NotificationManager()
for destination in sheet_data:
    flights = flight_search.get_flights_to(destination["iataCode"], tomorrow, six_month_from_today)

    cheapest_flight = find_cheapest_flight(flights)
    if cheapest_flight.price != "N/A":
        # if cheapest_flight.price < destination["lowestPrice"]
        print(f"{destination["city"]} : £{cheapest_flight.price}")
        notification_manager.send_flight_notification(cheapest_flight)
        notification_manager.send_email(customer_email_list,cheapest_flight)
    else :
        print(f"NO DIRECT FLIGHT for {destination["city"]}. LOOKING FOR INDIRECT...")
        stopover_flights = flight_search.get_flights_to(destination["iataCode"], tomorrow, six_month_from_today, False)

        cheapest_flight = find_cheapest_flight(stopover_flights)
        if cheapest_flight.price != "N/A":
            print(f"{destination["city"]} : £{cheapest_flight.price}")
            notification_manager.send_flight_notification(cheapest_flight)
            notification_manager.send_email(customer_email_list,cheapest_flight)
        else :
            print("NO INDIRECT AVAILABLE TOO.")
    time.sleep(1)