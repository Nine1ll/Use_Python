import requests
import os
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "8ED7Z23MK1O4XGVP"
NEWS_API_KEY = "791e477e438448fbb57b13e9f3d34d1b"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# https://console.twilio.com/?frameUrl=%2Fconsole%3Fx-target-region%3Dus1
# 키를 지속적으로 다시 받아야함

TWILIO_SID = "AC7b5a93187ca63b913e6d4638addbe412"
TWILIO_AUTH_TOKEN = '9642a0908b451da4adebcd8052362b39'

stock_parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'apikey': STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
data = response.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data['4. close'])
print(yesterday_closing_price)

the_day_before_data = data_list[1]
the_day_before_closing_price = float(the_day_before_data['4. close'])
print(the_day_before_closing_price)

difference = round(yesterday_closing_price - the_day_before_closing_price, 4)

up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

percentage = round((difference / yesterday_closing_price) * 100, 2)
print(percentage)

# Get News

if abs(percentage) > 1:

    news_parameters = {
        'q': COMPANY_NAME,
        'apiKey': NEWS_API_KEY
    }
    response_news = requests.get(NEWS_ENDPOINT, params=news_parameters)
    articles = response_news.json()['articles']
    three_articles = articles[:3]
    formatted_articles = [f"{STOCK_NAME}: {up_down}{percentage}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_='+19705362481',
            to='+821037089283'
        )
