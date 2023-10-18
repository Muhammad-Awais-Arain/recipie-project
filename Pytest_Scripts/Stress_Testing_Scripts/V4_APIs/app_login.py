import requests
from global_variable import dynamic_url
def app_login():
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
        'email': 'henry@mailinator.com',
        'password': 'henry'
    }

    try:
        response = requests.post(url, params=params, headers=headers, data=data)
        
        if response.status_code == 200:
            response_data = response.json()
            status = response_data.get('status')
            developer_message = response_data.get('developer_message')
            access_token = response_data.get('access_token')
            if status == 1 :
                return f"Status: {status}\nDeveloper Message: {developer_message}\nAccess Token: {access_token}\n"
            else:
                return f"Error: Invalid response format or data\nDevloper_Message: {developer_message}"
        else:
            response_data = response.json()
            developer_message = response_data.get('developer_message')
            return f"Login Error\nStatus Code: {response.status_code}\n Message: {developer_message}"

    except Exception as e:
        return f"Error: Invalid response format or data"

print(app_login())                                                      
