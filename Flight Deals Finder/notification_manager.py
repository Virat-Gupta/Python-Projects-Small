import requests
import os
from flight_data import FlightData
from dotenv import load_dotenv
load_dotenv()
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self) -> None:
        self.bot_token = os.environ["TELEGRAM_BOT_TOKEN"]
        self.bot_chatID = 'TELEGRAM_BOT_CHAT_ID'
    
    def send_flight_notification(self,data : FlightData):
        bot_message = f"Only £{data.price} to fly from {data.origin_airport} to {data.destination_airport}, on {data.out_date} until {data.return_date}."
        send_text = 'https://api.telegram.org/bot' + self.bot_token + '/sendMessage?chat_id=' + self.bot_chatID + '&parse_mode=Markdown&text=' + bot_message
        response = requests.get(send_text)
        print(response.json())
