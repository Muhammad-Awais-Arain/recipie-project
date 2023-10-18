import requests
from global_variable import dynamic_url

def get_navigation():
    api_url = dynamic_url

    url = f'{api_url}/rest_api/navigation'
    params = {
        'app_id': '118',
        'language': 'en'
    }
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'version': '0'
    }

    response = requests.post(url, params=params, headers=headers, data=data)

    if response.status_code == 200:
        data = response.json()
        status = data.get('status')
        developer_message = data.get('developer_message')

        if status == 1 and developer_message == "Get Navigation Successful":
            return (f"Status: {status}\nDeveloper Message: {developer_message}")
        else:
            return (f"Error in response. Status: {status}\nDeveloper Message: {developer_message}")
    else:
        return (f"Navigation Error: {response.status_code}")

