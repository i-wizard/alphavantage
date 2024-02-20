import asyncio
import os
import time

import aiohttp

result = []

def create_tasks(session):
    api_key = os.getenv("API_KEY")
    url = url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'
    symbols = ["AAPL", "MSFT", "GOOG", "TSLA", "AAPL", "MSFT", "GOOG", "TSLA", "AAPL", "MSFT", "GOOG", "TSLA"]
    tasks = []
    for symbol in symbols:
        print(f"working on {symbol}...")
        response = session.get(url.format(symbol, api_key), ssl=False)
        tasks.append(response)
    return tasks

async def pull_data():
    
    async with aiohttp.ClientSession() as session:
        tasks = create_tasks(session)
        responses = await asyncio.gather(*tasks)
        for response in responses:
            result.append(await response.json())
start = time.perf_counter()
asyncio.run(pull_data())
# loop = asyncio.get_event_loop()
# loop.run_until_complete(pull_data())
# loop.close()
end = time.perf_counter()

total = end - start
print(f"time taken {total} seconds to make {len(result)} calls")


