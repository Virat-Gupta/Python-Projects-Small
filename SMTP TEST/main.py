import smtplib
import datetime as dt
import random
import os

my_email = os.environ.get("EMAIL_AUTO")
my_pass = os.environ.get("EMAIL_AUTO_PASS")
reciever_email = "EMAIL HERE"

now = dt.datetime.now()
if now.weekday() == 0:
    quote = ""
    with open("Birthday Wisher smtp\\quotes.txt") as quote_file :
        quotes = quote_file.readlines()
        quote = random.choice(quotes)
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_pass)
        connection.sendmail(from_addr=my_email, to_addrs=reciever_email, msg=quote)