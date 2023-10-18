import os
import requests
import json
from deepdiff import DeepDiff 
from global_variable import dynamic_url

api_url = dynamic_url
BASE_URL = f'{api_url}/rest_api'

DATA_DIR = 'member_documents_responses'
DIFF_DIR = 'member_documents_differences'  # Specify the folder for differences

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

# Specify the range of app_ids
for app_id in range(118, 125):  # Change the range as needed
    # Create a folder named "app_responses" if it doesn't exist
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    # Create a folder named "membertool differences" if it doesn't exist
    if not os.path.exists(DIFF_DIR):
        os.makedirs(DIFF_DIR)

    # Function to compare two JSON objects and print the differences, including removed items
    def compare_json_objects(old_json, new_json, app_id):
        diff = DeepDiff(old_json, new_json, ignore_order=True)  # Compare while ignoring order of lists
        if not diff:
            return None  # No differences found
        else:
            return diff

    # Login and obtain access token and user ID
    email = 'henry@mailinator.com'
    password = 'henry'
    access_token, user_id = login(email, password, app_id)

    if access_token and user_id:
        # Specify the API URL and parameters for the current app_id
        api_url = f'{BASE_URL}/get_member_documents'
        params = {
            'app_id': app_id,
            'user_id': user_id,
            'language': 'en'
        } 

        # Define the request headers
        headers = {
            'accept': 'application/json',
            'Authorization': f'Bearer {access_token}'
        }

        # Construct the filename dynamically
        filename = os.path.join(DATA_DIR, f"user_id_{user_id}_app_id_{app_id}.json")

        # Check if the file exists before attempting to open it
        if os.path.exists(filename):
            # Use the POST method for the request
            response = requests.post(api_url, params=params, headers=headers)

            if response.status_code == 200:
                new_json_response = response.json()

                # Load the saved JSON response
                with open(filename, 'r') as file:
                    saved_json_response = json.load(file)

                print(f"Comparing responses for User ID {user_id} and App ID {app_id}:")
                differences = compare_json_objects(saved_json_response, new_json_response, app_id)
                if differences:
                    print(f"Differences found for User ID {user_id} and App ID {app_id}:")
                    print(json.dumps(differences, indent=4))

                    # Save the new JSON response with differences to a file in the "membertool differences" folder
                    diff_filename = os.path.join(DIFF_DIR, f"differences_user_id_{user_id}_app_id_{app_id}.json")
                    with open(diff_filename, 'w') as file:
                        json.dump(differences, file, indent=4)
                    print(f"New JSON response with differences saved to '{diff_filename}'")
                else:
                    print(f"No differences found for User ID {user_id} and App ID {app_id}.")
            else:
                print(f"Error: HTTP status code {response.status_code} for User ID {user_id} and App ID {app_id}")
                print(response.text)
        else:
            print(f"File not found: {filename}")
    else:
        print(f"Login failed for App ID {app_id}.")
