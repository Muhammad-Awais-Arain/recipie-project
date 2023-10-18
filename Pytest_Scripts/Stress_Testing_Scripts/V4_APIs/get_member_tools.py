import requests

from global_variable import dynamic_url
def get_member_tools(access_token, user_id):
    api_url = dynamic_url

    url = f'{api_url}/rest_api/get_member_tools'
    params = {
        'app_id': '118',
        'user_id': user_id,
        'language': 'en'
    }
    headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }

    try:
        response = requests.get(url, params=params, headers=headers)
        if response.status_code == 200:
            json_data = response.json()
            if json_data:
                return ('Member tools fetch successful')
                # Process the tools JSON data as needed
                # ...
            else:
                return ('Empty response')
        else:
            return (f'Request failed with status code: {response.status_code}')
            # Handle the failed request
    except requests.exceptions.RequestException as e:
        return ('An error occurred during the GET request:', e)
        # Handle the error
