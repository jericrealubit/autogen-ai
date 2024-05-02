# filename: stock_price_comparison.py
import pandas as pd
import matplotlib.pyplot as plt
import requests

# Function to fetch stock price data from Alpha Vantage API
def fetch_stock_data(symbol):
    api_key = 'YOUR_API_KEY'
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()['Time Series (Daily)']
    df = pd.DataFrame(data).T
    df.index = pd.to_datetime(df.index)
    df['4. close'] = pd.to_numeric(df['4. close'])
    return df

# Get stock price data for NVIDIA and TESLA
nvidia_data = fetch_stock_data('NVDA')
tesla_data = fetch_stock_data('TSLA')

# Plot the stock price change over time for both companies
plt.figure(figsize=(12, 6))
plt.plot(nvidia_data.index, nvidia_data['4. close'], label='NVIDIA')
plt.plot(tesla_data.index, tesla_data['4. close'], label='TESLA')
plt.title('NVIDIA vs TESLA Stock Price Change')
plt.xlabel('Date')
plt.ylabel('Stock Price (USD)')
plt.legend()
plt.grid(True)
plt.show()