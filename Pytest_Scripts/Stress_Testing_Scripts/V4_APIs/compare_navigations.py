import os
import requests
import json
from deepdiff import DeepDiff  
from global_variable import dynamic_url
# Specify the range of app_ids
for app_id in range(117, 120):  # Change the range as needed
    # Create a folder named "app_responses" if it doesn't exist
    if not os.path.exists("app_responses"):
        os.makedirs("app_responses")

    # Create a folder named "differences" if it doesn't exist
    if not os.path.exists("differences"):
        os.makedirs("differences")
    api_url = dynamic_url
  
    # Function to compare two JSON objects and print the differences, including removed items
    def compare_json_objects(old_json, new_json, app_id):
        
        diff = DeepDiff(old_json, new_json, ignore_order=True)  # Compare while ignoring order of lists
        if not diff:
            return None  # No differences found
        else:
            return diff

    # Specify the API URL and parameters for the current app_id
    api_url = f'{api_url}/rest_api/navigation?app_id={app_id}&language=en'

    # Define the request headers and data
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'version': '0',
    }

    # Make the POST request
    response = requests.post(api_url, headers=headers, data=data)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        new_json_response = response.json()

        # Load the saved JSON response
        saved_response_filename = os.path.join("app_responses", f"response_app_{app_id}.json")
        with open(saved_response_filename, 'r') as file:
            saved_json_response = json.load(file)

        print(f"Comparing responses for App_id {app_id}:")
        differences = compare_json_objects(saved_json_response, new_json_response, app_id)
        if differences:
            print(f"Differences found for App_id {app_id}:")
            print(json.dumps(differences, indent=4))

            # Save the new JSON response with differences to a file
            diff_filename = os.path.join("differences", f"differences_app_{app_id}.json")
            with open(diff_filename, 'w') as file:
                json.dump(differences, file, indent=4)
            print(f"New JSON response with differences saved to '{diff_filename}'")
        else:
            print(f"No differences found for App_id {app_id}.")
    else:
        print(f"Error: HTTP status code {response.status_code} for App_id {app_id}")
        print(response.text)
