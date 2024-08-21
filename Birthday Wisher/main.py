import smtplib
import pandas
import datetime
import random
import os

MY_EMAIL = os.environ.get("EMAIL_AUTO")
MY_PASS = os.environ.get("EMAIL_AUTO_PASS")

today = (datetime.datetime.now().month, datetime.datetime.now().day)

bithdays = pandas.read_csv("Birthday Wisher\\birthdays.csv")
birthday_dict = { (data_row["month"],data_row["day"]) : data_row for (index,data_row) in bithdays.iterrows()}

if today in birthday_dict:
    with open(f"Birthday Wisher\\letter_templates\\letter_{random.randint(1,3)}.txt") as letter:
        contents = letter.read()
        contents = contents.replace("[NAME]",birthday_dict[today]["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASS)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_dict[today]["email"], msg=f"Subject:Happy Birthday!\n\n{contents}")


# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.