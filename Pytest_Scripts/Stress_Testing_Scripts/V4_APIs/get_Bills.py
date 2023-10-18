import requests
import random
from global_variable import dynamic_url

def get_all_bills():
    api_url = dynamic_url

    url = f'{api_url}/rest_api/get_all_bills'
    params = {
        'app_id': '118',
        'language': 'en'
    }
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'category': '',
        'bill_id': '',
        'timestamp': ''
    }

    try:
        response = requests.post(url, params=params, headers=headers, data=data)
        response.raise_for_status()

        if response.status_code == 200:
            # Successful request
            json_data = response.json()
            # Process the JSON data as needed
            bills = json_data.get('data', [])
            if bills:
                random_bill = random.choice(bills)
                bill_id = random_bill.get('id')

                # Call the bill_submit API with the bill_id
                submit_bill_with_signature(bill_id)
                # Call the bill_view API with the bill_id
                bill_view(bill_id)
                # Call the learn_more API with the bill_id
                learn_more = get_bill_learn_more(bill_id)
                return f'All bills fetch successful.\nRandom Bill ID: {bill_id}\n\n{submit_bill_with_signature(bill_id)}\n{bill_view(bill_id)}\n{learn_more}'

            else:
                return ('No bills found')
        else:
            # Failed request
            return ('Request failed with status code:', response.status_code)

    except requests.exceptions.RequestException as e:
        return ('An error occurred:', e)


def submit_bill_with_signature(bill_id):
    url = 'https://desibook.admin.linkedunion.com/rest_api/bill_submit?app_id=118&user_id='
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'csrfmiddlewaretoken': 'LYdh4vRppShWyhraqShgU9Wwp8ERH47W4MV4AlCc4ixAu18NC8XbeBuY6afrKEBy',
        'testimony': 'Dear Senators,\nAs a concerned community member, I support Bill and urge your committee to pass the bill.\n\nMahalo\n',
        'signature': 'data:image/png;base64,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',  # You can provide the base64-encoded signature image data here
        'email': 'tayyab@linkedunion.com',
        'image': 'https://img.a.transfermarkt.technology/portrait/big/3139-1459504284.jpg?lm=1',
        'title': 'TEst',
        'user_id': '',
        'bill_id': bill_id,
    }

    try:
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()

        if response.status_code == 200:
            # Successful request
            return ('Bill submission successful')
        else:
            # Failed request
            return ('Bill submission failed with status code:', response.status_code)

    except requests.exceptions.RequestException as e:
        return ('An error occurred during bill submission:', e)


def bill_view(bill_id):
    url = f'https://desibook.admin.linkedunion.com/rest_api/bill_view?id={bill_id}&app_id=118&language=en'
    headers = {'accept': '*/*'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return ('View bill successful!')
    else:
        return (f"Failed to retrieve bill view. Status code: {response.status_code}")


def get_bill_learn_more(bill_id):
    url = f'https://desibook.admin.linkedunion.org/rest_api/bill_learn_more?id={bill_id}&app_id=118&language=en'
    headers = {'accept': '*/*'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200 and response.content:
        return ("Learn more bill fetch successful")
    else:
        return (f"Failed to fetch learn more. Status code: {response.status_code}")



print(get_all_bills())