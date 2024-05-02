# filename: stock_price_plot.py
import requests
import matplotlib.pyplot as plt
import pandas as pd

# Replace 'YOUR_API_KEY' with your actual Alpha Vantage API key
API_KEY = 'YOUR_API_KEY'
symbol_meta = 'META'
symbol_tesla = 'TSLA'

# Fetch historical stock prices for META
url_meta = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol_meta}&apikey={API_KEY}'
response_meta = requests.get(url_meta)
data_meta = response_meta.json()['Time Series (Daily)']

# Fetch historical stock prices for TESLA
url_tesla = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol_tesla}&apikey={API_KEY}'
response_tesla = requests.get(url_tesla)
data_tesla = response_tesla.json()['Time Series (Daily)']

# Extract dates and closing prices for META
dates_meta = []
prices_meta = []
for date, values in data_meta.items():
    dates_meta.append(date)
    prices_meta.append(float(values['4. close']))

# Extract dates and closing prices for TESLA
dates_tesla = []
prices_tesla = []
for date, values in data_tesla.items():
    dates_tesla.append(date)
    prices_tesla.append(float(values['4. close']))

# Create a DataFrame for META and TESLA stock prices
df_meta = pd.DataFrame({'Date': dates_meta, 'Price_META': prices_meta})
df_tesla = pd.DataFrame({'Date': dates_tesla, 'Price_TESLA': prices_tesla})

# Plot the stock price change over time for META and TESLA
plt.figure(figsize=(14, 7))
plt.plot(df_meta['Date'], df_meta['Price_META'], label='META', color='b')
plt.plot(df_tesla['Date'], df_tesla['Price_TESLA'], label='TESLA', color='r')
plt.title('META vs TESLA Stock Price Change')
plt.xlabel('Date')
plt.ylabel('Stock Price (USD)')
plt.xticks([])
plt.legend()
plt.grid(True)
plt.show()