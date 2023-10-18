import requests
from global_variable import dynamic_url

def get_notifications():
    api_url = dynamic_url

    url = f'{api_url}/rest_api/get_notifications'
    params = {
        'app_id': '118',
        'language': 'en'
    }
    headers = {
        'accept': 'application/json'
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        status = data.get('status')
        developer_message = data.get('developer_message')

        if status == 1 and developer_message == "Get notifications successful":
            return (f"Status: {status}\nDeveloper Message: {developer_message}")
        else:
            return (f"Error in response. Status: {status}\nDeveloper Message: {developer_message}")
    else:
        return (f"Notification Error: {response.status_code}")

