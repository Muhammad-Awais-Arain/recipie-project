import requests
from global_variable import dynamic_url
def get_all_news():
    api_url = dynamic_url

    url = f'{api_url}/rest_api/get_all_news'
    params = {
        'app_id': '118',
        'language': 'en'
    }
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'news_id': '',
        'category': '',
        'offset': '',
        'limit': '',
        'timestamp': ''
    }

    try:
        response = requests.post(url, params=params, headers=headers, data=data)
        response.raise_for_status()

        if response.status_code == 200:
            # Successful request
            json_data = response.json()
            status = json_data.get('status')
            developer_message = json_data.get('developer_message')

            if status == 1 and developer_message == "Get All News Successful":
                return (f"Status: {status}\nDeveloper Message: {developer_message}")
            else:
                return 'Error: Invalid response format or data'
        else:
            # Failed request
            return f"Request failed with status code: {response.status_code}"

    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"
