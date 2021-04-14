import requests
from twilio.rest import Client


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = ""
NEWS_API_KEY = ""
TWILIO_ACCOUNT_SID = ""
TWILIO_AUTH_TOKEN = ""


#TODO 1. Get yesterday's closing stock price.
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
# print(yesterday_closing_price)


#TODO 2. Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
# print(day_before_yesterday_closing_price)


#TODO 3. Find the positive difference between 1 and 2.
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
# print(difference)
if difference > 0:
    up_down = "🔼"
else:
    up_down = "🔽"


#TODO 4. Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percentage = round((difference / float(yesterday_closing_price)) * 100)
# print(diff_percentage)



#TODO 5. If difference percentage is greater than 5, then get articles related to company_name.
if abs(diff_percentage) > 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    # print(articles)


#TODO 6. Create a list that contains the first 3 articles.
three_articles = articles[:3]
# print(three_articles)


#TODO 7. Create a new list of the first 3 article's headline and description.
formatted_articles_list = [f"{STOCK_NAME}: {up_down}{diff_percentage}% \nYesterday's closing price: {yesterday_closing_price}$ \nDay before yesterday's closing price: {day_before_yesterday_closing_price}$ \nHeadline: {article['title']}. \nBreif: {article['description']}" for article in three_articles]


#TODO 8. - Send each article as a separate message via Twilio.
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

for article in formatted_articles_list:
    message = client.messages \
                    .create(
                        body=article,
                        from_='twilio experiment number',
                        to='your number'
                    )