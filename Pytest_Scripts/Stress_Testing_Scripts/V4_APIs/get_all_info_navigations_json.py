import os
import json
import requests
from global_variable import dynamic_url
api_url = dynamic_url

BASE_URL = f'{api_url}/rest_api/get_info_navigation'
HEADERS = {'accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}
DATA_DIR = './info_navigation_responses'  # Directory to store JSON responses


def get_info_navigation_data_for_app_id(app_id):
    params = {
        'app_id': app_id,
        'language': 'en'
    }

    data = {
        'version': '0'
    }

    response = requests.post(BASE_URL, headers=HEADERS, params=params, data=data)
    if response.status_code == 200:
        info_navigation_data = response.json()
        status = info_navigation_data.get('status')
        developer_message = info_navigation_data.get('developer_message')
        if status == 1 and "Get Info Navigation Successful" in developer_message:
            print(f"Info Navigation API for App_id {app_id} is up and functioning correctly.")
            # Save the JSON response to a file
            filename = f'{DATA_DIR}/app_id{app_id}.json'
            with open(filename, 'w') as f:
                json.dump(info_navigation_data, f, indent=2)
        else:
            return (f"Info Navigation API for app_id {app_id} is not functioning correctly. Developer message: {developer_message}")
    else:
        return (f"Failed to fetch info navigation data for app_id {app_id}, status code: {response.status_code}")


def get_all_info_navigation():
    app_ids_without_success = []
    for app_id in range(117, 120):
        result = get_info_navigation_data_for_app_id(app_id)
        if result is not None:
            app_ids_without_success.append(result)

    if app_ids_without_success:
        return ("App IDs not returning 'Get Info Navigation Successful':", app_ids_without_success)
    else:
        return ("Info Navigation API for all app IDs are up and functioning correctly.")


# Create the data directory if it does not exist
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

name = get_all_info_navigation()
print(name)
