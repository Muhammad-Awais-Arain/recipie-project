import requests
from global_variable import dynamic_url
api_url = dynamic_url

BASE_URL = f'{api_url}/rest_api/get_all_website_home_page_section'
HEADERS = {'accept': 'application/json'}


def get_data_for_app_id(app_id):
    params = {
        'app_id': app_id,
        'user_id': 6276272,
        'language': 'en'
    }

    response = requests.post(BASE_URL, headers=HEADERS, params=params, data={})
    if response.status_code == 200 and 'status' in response.json() and 'developer_message' in response.json():
        status = response.json()['status']
        developer_message = response.json()['developer_message']
        if status == 1:
            print(f"Received data for app_id {app_id}")
        else:
            print(f"Backend for app_id {app_id} is up but returned status -1. Developer message: {developer_message}")
            return app_id
    else:
        print(f"Failed to fetch data for app_id {app_id}, status code: {response.status_code}")
        return app_id


def get_all_homesections():
    app_ids_without_data = []
    for app_id in range(1, 585):
        result = get_data_for_app_id(app_id)
        if result is not None:
            app_ids_without_data.append(result)

    if app_ids_without_data:
        return f"App IDs with not returning home sections: {app_ids_without_data}"
    else:
        return "All Home Sections returned data successfully."
