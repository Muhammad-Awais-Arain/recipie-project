import requests
from global_variable import dynamic_url
def get_elected_official():
    api_url = dynamic_url

    url = f'{api_url}/rest_api/get_my_elected_official?search_address=5525%20EAST%20AVE%20T'
    headers = {
        'accept': 'application/json'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        status = 1
        developer_message = 'Get Elected Official Successful'
    else:
        status = response.status_code
        developer_message = 'Error: Failed to get elected official'

    return f"Status: {status}\nDeveloper Message: {developer_message}"

print (get_elected_official())

