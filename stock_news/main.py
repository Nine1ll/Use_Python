import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
APT_KEY = "8ED7Z23MK1O4XGVP"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'apikey': APT_KEY
}

# Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries.

response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
data = response.json()['Time Series (Daily)']

data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data['4. close']
print(yesterday_closing_price)

# Get the day before yesterday's closing stock price

the_day_before_yesterday_data = data_list[1]
the_day_before_yesterday_closing_price = the_day_before_yesterday_data['4. close']
print(the_day_before_yesterday_closing_price)


# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.

positive_difference = round(abs(float(yesterday_closing_price)-float(the_day_before_yesterday_closing_price)), 4)
print(positive_difference)

# TODO 4. - Work out the percentage difference in price between closing price yesterday
# and closing price the day before yesterday.


# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

# # STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# TODO 6. - Instead of printing ("Get News"),
# use the News API to get articles related to the COMPANY_NAME.

# TODO 7. - Use Python slice operator to create a list that contains the first 3 articles.
# Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


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

