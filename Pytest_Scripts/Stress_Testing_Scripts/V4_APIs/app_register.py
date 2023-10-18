import requests
from global_variable import dynamic_url
def app_register():
    api_url = dynamic_url

    url = f'{api_url}/rest_api/app_register'
    params = {
        'app_id': '118',
        'language': 'en'
    }
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'first_name': 'Hassan',
        'last_name': 'SQA',
        'email': 'hassan@linkedunion.com',
        'password': '123',
        'employee_id': '010101',
        'date_of_birth': '05/24/1999'
    }

    try:
        response = requests.post(url, params=params, headers=headers, data=data)
        
        if response.status_code == 200:
            response_data = response.json()
            status = response_data.get('status')
            developer_message = response_data.get('developer_message')
            id = response_data.get('id')
            if status == 1:
                return f"Status: {status}\nDeveloper Message: {developer_message}\nID: {id}"
            else:
                return f"Error: Invalid response format or data\nDeveloper Message: {developer_message}"
        else:
            response_data = response.json()
            developer_message = response_data.get('developer_message')
            return f"Registration Error\nStatus Code: {response.status_code}\nDeveloper Message: {developer_message}"

    except Exception as e:
        return f"Error: Invalid response format or data"

# Call the function directly
print(app_register())
