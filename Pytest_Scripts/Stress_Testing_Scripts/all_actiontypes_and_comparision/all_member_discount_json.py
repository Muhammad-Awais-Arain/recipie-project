import os
import requests
import json
from deepdiff import DeepDiff

from global_variable import dynamic_url
api_url = dynamic_url
# Define the range of app_ids
app_id_range = range(117, 120)

# Create a directory to save responses if it doesn't exist
if not os.path.exists("discount_responses"):
    os.makedirs("discount_responses")

# Iterate over each app_id
for app_id in app_id_range:
    # Define the API endpoint URL
    url = f'{api_url}/rest_api/get_member_discounts?app_id={app_id}&language=en'

    # Make a POST request
    response = requests.post(
        url,
        headers={
            'accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        data={
            'discount_id': '',
            'category': '',
            'timestamp': ''
        }
    )
    # Check if the request was successful
    if response.status_code == 200:
        # Save the JSON response to a separate file
        response_data = response.json()
        with open(f'discount_responses/app_{app_id}_response.json', 'w') as file:
            json.dump(response_data, file, indent=4)
        
        # Print a message indicating success
        print(f'Navigation(member discounts) for App_id {app_id} is up and functioning correctly.')

    else:
        # Print a message indicating failure
        print(f'Navigation(member discounts) for App_id {app_id} is not up and not functioning correctly.')

