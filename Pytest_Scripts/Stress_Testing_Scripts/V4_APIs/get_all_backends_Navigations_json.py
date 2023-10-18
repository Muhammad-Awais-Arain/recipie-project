import os
import requests
import json
from global_variable import dynamic_url
# Specify the range of app_ids
for app_id in range(117, 120):  
    api_url = dynamic_url
    # Create a folder named "app_responses" if it doesn't exist
    if not os.path.exists("app_responses"):
        os.makedirs("app_responses")

    api_url = f'{api_url}/rest_api/navigation?app_id={app_id}&language=en'

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'version': '0',
    }

   
    response = requests.post(api_url, headers=headers, data=data)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        json_response = response.json()

        # Save the JSON response to a file in the "app_responses" folder
        filename = os.path.join("app_responses", f"response_app_{app_id}.json")
        with open(filename, 'w') as file:
            json.dump(json_response, file, indent=4)

        print(f"Navigation API for App_id {app_id} is up and functioning correctly.")
        print(f"JSON response saved to '{filename}'")
    else:
        print(f"Navigation API for App_id {app_id} is not up and not functioning correctly.")
        print(f"Error: HTTP status code {response.status_code}")
        print(response.text)
