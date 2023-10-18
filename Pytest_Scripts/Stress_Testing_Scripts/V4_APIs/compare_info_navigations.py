import os
import json
import requests
from deepdiff import DeepDiff
from global_variable import dynamic_url
api_url = dynamic_url
BASE_URL = f'{api_url}/rest_api/get_info_navigation'
HEADERS = {'accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}
DATA_DIR = './info_navigation_responses'
DIFF_DIR = './info_navigation_differences'

def compare_json_objects(old_json, new_json, app_id):
    # Ignore 'nid' and value changes, only capture structural and key name differences
    exclude_paths = ["root['version']", "root['nid']"]
    diff = DeepDiff(old_json, new_json, exclude_paths=exclude_paths, ignore_order=True)
    if not diff:
        return None
    else:
        return diff

def compare_info_navigation_for_app_id(app_id):
    saved_response_filename = os.path.join(DATA_DIR, f'app_id{app_id}.json')
    with open(saved_response_filename, 'r') as file:
        saved_json_response = json.load(file)

    params = {
        'app_id': app_id,
        'language': 'en'
    }
    data = {
        'version': '0'
    }
    response = requests.post(BASE_URL, headers=HEADERS, params=params, data=data)

    if response.status_code == 200:
        new_json_response = response.json()
        differences = compare_json_objects(saved_json_response, new_json_response, app_id)
        if differences:
            print(f"Differences found for App_id {app_id}:")
            print(json.dumps(differences, indent=4))

            check_for_additions_deletions(saved_json_response, new_json_response)

            diff_filename = os.path.join(DIFF_DIR, f'differences_app_id{app_id}.json')
            with open(diff_filename, 'w') as file:
                json.dump(differences, file, indent=4)
            print(f"New JSON response with differences saved to '{diff_filename}'")
        else:
            print(f"No differences found for App_id {app_id}.")
    else:
        print(f"Error: HTTP status code {response.status_code} for App_id {app_id}")
        print(response.text)

def check_for_additions_deletions(old_json, new_json):
    # Check for additions
    for key, value in new_json.items():
        if key not in old_json:
            print(f"Added: {key} - {value}")

    # Check for deletions
    for key, value in old_json.items():
        if key not in new_json:
            print(f"Removed: {key} - {value}")

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)
if not os.path.exists(DIFF_DIR):
    os.makedirs(DIFF_DIR)

for app_id in range(117, 120):
    compare_info_navigation_for_app_id(app_id)
