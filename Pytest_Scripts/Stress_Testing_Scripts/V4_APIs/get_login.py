import requests
from global_variable import dynamic_url

def login(email, password):
    api_url = dynamic_url

    url = f'{api_url}/rest_api/login'
    params = {
        'app_id': '118',
        'language': 'en'
    }
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'email': email,
        'password': password
    }

    try:
        response = requests.post(url, params=params, headers=headers, data=data)
        response.raise_for_status()
        json_data = response.json()
        access_token = json_data['access_token']
        user_id = json_data['data']['id']
        # print(f'{access_token} {user_id}')
        return access_token, user_id
    except requests.exceptions.RequestException as e:
        print('An error occurred during login:', e)
        return None, None
