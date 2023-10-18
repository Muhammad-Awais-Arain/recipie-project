import os
import requests
import json
from deepdiff import DeepDiff

from global_variable import dynamic_url

for app_id in range(117, 120):  
    # Create a folder named "news_responses" if it doesn't exist
    if not os.path.exists("news_responses"):
        os.makedirs("news_responses")

    # Create a folder named "news_differences" if it doesn't exist
    if not os.path.exists("news_differences"):
        os.makedirs("news_differences")

    api_url = dynamic_url

    # Function to compare two JSON objects and print the differences, including removed items
    def compare_json_objects(old_json, new_json, app_id):
        diff = DeepDiff(old_json, new_json, ignore_order=True)  
        if not diff:
            return None 
        else:
            return diff

    api_url = f'{api_url}/rest_api/get_all_news?app_id={app_id}&language=en'

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'version': '0',
    }

    response = requests.post(api_url, headers=headers, data=data)

    if response.status_code == 200:
        # Parse the JSON response
        new_json_response = response.json()

        # Load the saved JSON response, assuming the naming convention "app_{app_id}_response.json"
        saved_response_filename = os.path.join("news_responses", f"app_{app_id}_response.json")
        if os.path.exists(saved_response_filename):
            with open(saved_response_filename, 'r') as file:
                saved_json_response = json.load(file)

            # Make a copy of the new JSON response
            new_response_copy = new_json_response.copy()

            print(f"Comparing responses for App_id {app_id}:")
            differences = compare_json_objects(saved_json_response, new_json_response, app_id)
            if differences:
                print(f"Differences found for App_id {app_id}:")
                print(json.dumps(differences, indent=4))

                # Save the new JSON response with differences to a file in "news_differences" folder
                diff_filename = os.path.join("news_differences", f"app_{app_id}_differences.json")
                with open(diff_filename, 'w') as file:
                    json.dump(differences, file, indent=4)
                print(f"New JSON response with differences saved to '{diff_filename}'")

             
            else:
                print(f"No differences found for App_id {app_id}.")
        else:
            print(f"No saved response found for App_id {app_id}. Saving the current response.")

    else:
        print(f"Error: HTTP status code {response.status_code} for App_id {app_id}")
        print(response.text)
