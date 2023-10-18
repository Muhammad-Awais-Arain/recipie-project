import requests
import csv
from website_domains_production import DOMAINS

def get_app_id(domain):
    url = f'https://desibook.admin.linkedunion.com/rest_api/get_app_id?url={domain}'
    headers = {'accept': 'application/json'}
    response = requests.get(url, headers=headers)
    return response.json()

def main():
    domains = DOMAINS
    null_domains = []

    with open('null_domains.csv', 'w', newline='') as csvfile:
        fieldnames = ['Domain']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for domain in domains:
            result = get_app_id(domain)
            if result['status'] == 1:
                app_id = result['data']['app_id']
                app_name = result['data']['app_name']
                print(f'Domain: {domain}, App ID: {app_id}, App Name: {app_name}')
            else:
                print(f'Domain: {domain}, No data returned.')
                null_domains.append(domain)
                writer.writerow({'Domain': domain})

    print('Script execution completed.')


if __name__ == "__main__":
    main()
