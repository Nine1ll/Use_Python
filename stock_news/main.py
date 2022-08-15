import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "8ED7Z23MK1O4XGVP"
NEWS_API_KEY = "791e477e438448fbb57b13e9f3d34d1b"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

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

positive_difference = round(abs(yesterday_closing_price - the_day_before_closing_price), 4)
print(positive_difference)

percentage = round((positive_difference/the_day_before_closing_price)*100,2)
print(percentage)

date = list(response.json()['Time Series (Daily)'].keys())

# Get News

news_parameters = {
    'q': COMPANY_NAME,
    'from': date,
    'apiKey': NEWS_API_KEY
}

if True: # percentage > 5
    response_news = requests.get(NEWS_ENDPOINT, params=news_parameters)
    news = response_news.json()['articles'][:3]
    headlines = [news_dict['title'] for news_dict in news]
    print(headlines)

# # STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

# TODO 8. - Create a new list of the first 3 article's headline
# and description using list comprehension.


# TODO 9. - Send each article as a separate message via Twilio.

# Optional
# TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

