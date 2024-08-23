import requests
import os
import datetime
from newsapi import NewsApiClient
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_PRICE_API_KEY = os.environ.get("APLHA_API_KEY")

NEWS_API_KEY  = os.environ.get("NEWS_API_KEY")

account_sid = os.environ.get("TWILIO_ACCOUTN_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

from_phone = os.environ.get("FROM_PH")
to_phone : str = os.environ.get("TO_PH") # type: ignore

parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_PRICE_API_KEY,
}
data = requests.get(url=STOCK_ENDPOINT, params=parameters)


today_date = datetime.datetime.now().date()
yesterday = today_date - datetime.timedelta(1)
before_yesterday = yesterday - datetime.timedelta(1)

yesterday_closing = float(data.json()["Time Series (Daily)"][str(yesterday)]["4. close"])

before_yesterday_closing = float(data.json()["Time Series (Daily)"][str(before_yesterday)]["4. close"])

difference = yesterday_closing - before_yesterday_closing
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

percentage_difference = abs(difference)/yesterday_closing * 100.0 

if percentage_difference > 5 :
    newsapi = NewsApiClient(api_key=NEWS_API_KEY)
    all_articles = newsapi.get_everything(qintitle=COMPANY_NAME, language='en', sort_by='relevancy')
    article_list = all_articles["articles"][:3]

    formatted_articles = [f"\n{STOCK_NAME}: {up_down}{percentage_difference : 5.2f}%\nHeadline : {article['title']}. \nBrief : {article['description']}" for article in article_list]

    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=from_phone,
            to=to_phone,
        )