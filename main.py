import os
import time

import requests

result = []

def pull_data():
    api_key = os.getenv("API_KEY")
    url = url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'
    symbols = ["AAPL", "MSFT", "GOOG", "TSLA", "AAPL", "MSFT", "GOOG", "TSLA", "AAPL", "MSFT", "GOOG", "TSLA"]
    
    for symbol in symbols:
        print(f"working on {symbol}...")
        response = requests.get(url.format(symbol, api_key))
        result.append(response.json())
start = time.perf_counter()
pull_data()
end = time.perf_counter()

total = end - start
print(f"time taken {total} seconds to make {len(result)} calls")


