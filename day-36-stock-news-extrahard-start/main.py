import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "tesla"

STOCK_API_KEY = "hidden"
STOCK_URL = 'https://www.alphavantage.co/query'

NEWS_API_KEY = "hidden"
NEWS_URL = 'https://newsapi.org/v2/everything'

TWILIO_SID = 'hidden'
TWILIO_AUTO_TOKEN = 'hidden'


def stock_price_change(yesterday_close, the_day_before_yesterday_close):
    return (yesterday_close - the_day_before_yesterday_close) / the_day_before_yesterday_close * 100


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_parameters = {"function": "TIME_SERIES_DAILY",
                    "symbol": STOCK,
                    "apikey": STOCK_API_KEY}

response_stock = requests.get(STOCK_URL, params=stock_parameters)
daily_info = response_stock.json()["Time Series (Daily)"]
data_key = list(daily_info.keys())  # Create a list of the dict keys

yesterday_close = float(daily_info[data_key[0]]['4. close'])  # 0: yesterday
the_day_before_yesterday_close = float(daily_info[data_key[1]]['4. close'])  # 1: the day before yesterday


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
if abs(stock_price_change(yesterday_close, the_day_before_yesterday_close)) <= 5:
    news_parameters = {
        'q': COMPANY_NAME,
        'from': f'{data_key[0]}',  # yesterday date
        'sortBy': 'publishedAt',
        'apiKey': NEWS_API_KEY,
        'language': 'en'
    }

    response_news = requests.get(NEWS_URL, params=news_parameters)
    data_news = response_news.json()
    recent_3_articles = data_news['articles'][:3]

    ## STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.

    formatted_msg_contents = [f"Headline: {article['title']}. \nBrief: {article['description']}"
                              for article in recent_3_articles]

    client = Client(TWILIO_SID, TWILIO_AUTO_TOKEN)
    for msg in formatted_msg_contents:
        message = client.messages.create(
            body=msg,
            from_= '+12345678',
            to= '+12345678'
        )
    #Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

