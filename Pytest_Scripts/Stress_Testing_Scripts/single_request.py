import csv
import time
import asyncio
import aiohttp
from bs4 import BeautifulSoup

# Specify the URLs to open multiple times
urls = ["https://teamsterslocal320.org/"]

# Specify the number of times to open each website
num_times = 500

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

async def fetch(session, url):
    start_time = time.time()

    try:
        async with session.get(url, headers=headers, timeout=aiohttp.ClientTimeout(total=120)) as response:
            soup = BeautifulSoup(await response.text(), 'html.parser')
            title = soup.title.text if soup.title else "N/A"
            end_time = time.time()
            load_time = end_time - start_time
    except asyncio.TimeoutError:
        title = "Timeout Error"
        url = "N/A"
        load_time = None

    return title, url, load_time

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            for i in range(num_times):
                task = asyncio.ensure_future(fetch(session, url))
                tasks.append(task)

        results = await asyncio.gather(*tasks)

        with open('Single_Request.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Website No", "Title", "URL", "Load Time (seconds)"])

            for i, (title, url, load_time) in enumerate(results):
                row = [i + 1, title, url, load_time]
                writer.writerow(row)
                print(f"Website No: {i + 1}, Load Time: {load_time} seconds")

    print("Results written to Single_Request.csv")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
