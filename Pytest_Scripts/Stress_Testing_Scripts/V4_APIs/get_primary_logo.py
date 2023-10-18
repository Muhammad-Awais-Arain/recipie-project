import requests
import json
import os

def check_url_status(url):
    response = requests.head(url)

    return response.status_code == 200

def get_image_url(api_url, app_id, image_key):
    # Make a GET request to the API
    response = requests.get(api_url.format(app_id=app_id), headers={'accept': 'application/json'})

    if response.status_code == 200:
        data = response.json()

        image_url = data.get('data', {}).get(image_key)

        if image_url and check_url_status(image_url):
            return None  
        else:
            return {'app_id': app_id, 'image_key': image_key, 'image_url': image_url}
    else:
        return {'app_id': app_id, 'error': f"Unable to fetch data from API. Status code: {response.status_code}"}

def main():
    api_url = 'https://admin.linkedunion.com/rest_api/get_app_appearance?app_id={app_id}&language=en'

    app_id_list = [
        104, 68, 103, 113, 391, 362, 159, 192, 398, 195, 353, 161, 69, 67, 134, 399, 194, 158, 355, 397, 151, 169, 156,
        273, 245, 242, 221, 210, 243, 244, 272, 281, 257, 401, 266, 259, 235, 232, 204, 203, 260, 258, 256, 400, 269,
        202, 233, 234, 174, 180, 379, 20, 9, 377, 348, 142, 7, 29, 16, 129, 116, 73, 6, 385, 143, 188, 382, 10, 186,
        19, 8, 181, 313, 121, 119, 86, 314, 110, 43, 325, 198, 153, 38, 395, 359, 392, 162, 31, 165, 91, 136, 332,
        100, 107, 138, 30, 369, 190, 164, 351, 163, 197, 358, 199, 394, 360, 334, 106, 99, 139, 101, 137, 108, 284,
        248, 277, 241, 279, 278, 247, 249, 271, 222, 207, 405, 254, 291, 265, 239, 208, 237, 264, 255, 79, 320, 318,
        41, 327, 83, 311, 123, 177, 183, 23, 373, 15, 374, 12, 179, 85, 71, 317, 82, 122, 40, 319, 114, 326, 47, 113,
        78, 147, 2, 178, 13, 140, 14, 182, 344, 176, 22, 149, 343, 185, 25, 160, 257, 257,
    ]

    image_keys = ['primary_logo_image', 'app_background_image']

    missing_primary_logos = []
    invalid_primary_logo_status = []
    missing_background_images = []
    invalid_background_image_status = []

    for app_id in app_id_list:
        for key in image_keys:
            # Get information about the image for each app_id and key
            result = get_image_url(api_url, app_id, key)

            if result:
                if 'error' in result:
                    if key == 'primary_logo_image':
                        invalid_primary_logo_status.append(result)
                    elif key == 'app_background_image':
                        invalid_background_image_status.append(result)
                else:
                    if key == 'primary_logo_image':
                        missing_primary_logos.append(result)
                    elif key == 'app_background_image':
                        missing_background_images.append(result)

    folder_name = 'logo_and_background_image_responses'
    os.makedirs(folder_name, exist_ok=True)

    output_data_primary_logo = {'missing_primary_logos': missing_primary_logos, 'invalid_primary_logo_status': invalid_primary_logo_status}
    output_data_background_image = {'missing_background_images': missing_background_images, 'invalid_background_image_status': invalid_background_image_status}

    primary_logo_file_path = os.path.join(folder_name, 'primary_logo_check_results.json')
    background_image_file_path = os.path.join(folder_name, 'background_image_check_results.json')

    with open(primary_logo_file_path, 'w') as json_file:
        json.dump(output_data_primary_logo, json_file, indent=2)

    with open(background_image_file_path, 'w') as json_file:
        json.dump(output_data_background_image, json_file, indent=2)

if __name__ == "__main__":
    main()
