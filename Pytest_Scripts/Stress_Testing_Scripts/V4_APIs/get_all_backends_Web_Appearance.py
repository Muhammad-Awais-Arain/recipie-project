import requests
import concurrent.futures
from global_variable import dynamic_url
api_url = dynamic_url

app_ids = [str(i) for i in range(1, 500)]  # create a list of app IDs from 1 to 250

base_url = f'{api_url}/rest_api/get_web_appearance?app_id='


def send_request(url):
    response = requests.get(url)
    print(response.status_code)
    return response.status_code


urls = [f"{base_url}{app_id}&language=en" for app_id in app_ids]  # create a list of URLs with app IDs inserted
print(urls)

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = list(executor.map(send_request, urls))

print(results)
