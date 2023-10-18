import requests
from global_variable import dynamic_url
def forgot_password():
    api_url = dynamic_url

    url = f'{api_url}/rest_api/forgot_password'
    params = {
        'app_id': '118',
        'language': 'en'
    }
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'email': 'henry@mailinator.com'
    }

    try:
        response = requests.post(url, params=params, headers=headers, data=data)
        
        if response.status_code == 200:
            response_data = response.json()
            status = response_data.get('status')
            developer_message = response_data.get('developer_message')
            return f"Status: {status}\nDeveloper Message: {developer_message}"
        else:
            response_data = response.json()
            developer_message = response_data.get('developer_message')
            status = response_data.get('status')
            return f"Error: {developer_message}\nStatus: {status}\nStatus Code: {response.status_code}"

    except Exception as e:
        return f"Error: Invalid response format or data."

print(forgot_password())
