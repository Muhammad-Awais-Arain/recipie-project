import requests
from global_variable import dynamic_url
def get_member_discounts():
    api_url = dynamic_url

    url = f'{api_url}/rest_api/get_member_discounts'
    params = {
        'app_id': '118',
        'language': 'en',
    }
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'contact_id': '',
        'category': '',
        'timestamp': ''
    }

    response = requests.post(url, params=params, headers=headers, data=data)

    if response.status_code == 200:
        data = response.json()
        status = data.get('status')
        developer_message = data.get('developer_message')
        if status == 1 and developer_message == "Get Member Discounts Successful":
         return (f"Status: {status}\nDeveloper Message: {developer_message}")
        else:
            return "Error: Invalid response format or data"
    else:

        return f"Get All Member Discounts Error: {response.status_code}"
print (get_member_discounts())
