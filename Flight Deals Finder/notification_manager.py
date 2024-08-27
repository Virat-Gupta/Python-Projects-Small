import requests
import os
import smtplib
from flight_data import FlightData
from dotenv import load_dotenv
load_dotenv()
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self) -> None:
        self.bot_token = os.environ["TELEGRAM_BOT_TOKEN"]
        self.bot_chatID = os.environ['TELEGRAM_BOT_CHAT_ID']
        self.smtp_address = os.environ["EMAIL_PROVIDER_SMTP_ADDRESS"]
        self.email = os.environ["MY_EMAIL"]
        self.email_password = os.environ["MY_EMAIL_PASSWORD"]
    
    def send_flight_notification(self,data : FlightData):
        bot_message = f"Only £{data.price} to fly from {data.origin_airport} to {data.destination_airport}, on {data.out_date} until {data.return_date}."
        send_text = 'https://api.telegram.org/bot' + self.bot_token + '/sendMessage?chat_id=' + self.bot_chatID + '&parse_mode=Markdown&text=' + bot_message
        response = requests.get(send_text)
        print(response.json())
    
    def send_email(self, email_list, data : FlightData):
        bot_message = f"Only £{data.price} to fly from {data.origin_airport} to {data.destination_airport}, on {data.out_date} until {data.return_date}."
        with smtplib.SMTP((os.environ["EMAIL_PROVIDER_SMTP_ADDRESS"])) as self.connection:
            self.connection.starttls()
            self.connection.login(self.email, self.email_password)
            for email in email_list:
                self.connection.sendmail(from_addr=self.email,
                                        to_addrs=email,
                                         msg=f"Subject:New Low Price Flight!\n\n{bot_message}".encode('utf-8'))

