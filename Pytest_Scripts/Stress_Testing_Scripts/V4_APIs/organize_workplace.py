import requests
import json
from global_variable import dynamic_url
def organize_workplace():
    api_url = dynamic_url

    url = f'{api_url}/rest_api/organize_workplace'
    params = {
        'app_id': '118',
        'user_id': '123',
        'language': 'en'
    }
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    data = {
        "fname": "Henry",
        "lname": "Smith",
        "email": "hassan@gmail.com",
        "phone": "123321",
        "employer": "LinkedUnion",
        "occupation": "SQA",
        "country": "Pakistan",
        "address": "B-16/487",
        "state": "Sindh",
        "city": "Karachi",
        "postal": "123",
        "peoplework": "55",
        "issues": "This issue is only for testing purpose,kindly ignore!"
    }

    try:
        response = requests.post(url, params=params, headers=headers, json=data)
        
        if response.status_code == 200:
            response_data = response.json()
            status = response_data.get('status')
            developer_message = response_data.get('developer_message')
            if status == 1 and developer_message == "SUCCESS! THANK YOU, YOUR REQUEST SUBMITTED!":
                return f"Form Data: {json.dumps(data)}\n \nStatus: {status}\nDeveloper Message: {developer_message}\n"
            else:
                return "Error: Invalid response format or data"
        else:
            return f"Get Organize Workplace Error: {response.status_code}"

    except Exception as e:
        return f"Error: {str(e)}"

print(organize_workplace())
