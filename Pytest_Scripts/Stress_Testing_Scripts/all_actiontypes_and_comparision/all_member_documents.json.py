import os
import json
import requests

from global_variable import dynamic_url

api_url = dynamic_url
BASE_URL = f'{api_url}/rest_api'
HEADERS = {'accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}
DATA_DIR = 'member_documents_responses'

def login(email, password, app_id):
    url = f'{BASE_URL}/login'
    params = {
        'app_id': app_id,
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
        
        if 'data' in json_data and 'id' in json_data['data']:
            access_token = json_data['access_token']
            user_id = json_data['data']['id']
            return access_token, user_id
        else:
            return None, None

    except requests.exceptions.RequestException as e:
        print('An error occurred during login:', e)
        return None, None

def get_member_documents_data(access_token, user_id, app_id):
    url = f'{BASE_URL}/get_member_documents'
    params = {
        'app_id': app_id,
        'user_id': user_id,
        'language': 'en'
    }

    headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }

    try:
        response = requests.post(url, params=params, headers=headers)
        if response.status_code == 200:
            tools_data = response.json()
            status = tools_data.get('status')
            developer_message = tools_data.get('developer_message')
            
            print(f"Member documents API for User ID {user_id} and App ID {app_id} response received.")

            # Save the JSON response to a file
            filename = f'{DATA_DIR}/user_id_{user_id}_app_id_{app_id}.json'
            with open(filename, 'w') as f:
                json.dump(tools_data, f, indent=2)

            if status == 1:
                print(f"Member documents API for User ID {user_id} and App ID {app_id} is up and functioning correctly.")
                return True
            else:
                print(f"Member documents API for User ID {user_id} and App ID {app_id} is not functioning correctly. Developer message: {developer_message}")
                return False
        else:
            print(f"Failed to fetch Member documents data for User ID {user_id} and App ID {app_id}, status code: {response.status_code}")
            return False

    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the POST request: {e}")
        return False

def get_all_member_documents(email, password):
    app_ids_with_user = []
    app_ids_without_user = []

    for app_id in range(118, 125):
        access_token, user_id = login(email, password, str(app_id))
        if access_token and user_id:
            result = get_member_documents_data(access_token, user_id, str(app_id))
            if result:
                app_ids_with_user.append(app_id)
            else:
                app_ids_without_user.append(app_id)
        else:
            app_ids_without_user.append(app_id)

    return app_ids_with_user, app_ids_without_user

# Create a directory if it doesn't exist
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

email = 'henry@mailinator.com'
password = 'henry'
member_documents_output = get_all_member_documents(email, password)

# Check if any app_ids were successful
if member_documents_output[0]:
    print("Member documents APIs are up and functioning correctly for app IDs:", member_documents_output[0])
else:
    print("No user found in app IDs:", member_documents_output[1])
