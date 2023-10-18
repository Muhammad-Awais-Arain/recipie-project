import csv
import requests
import concurrent.futures
import time
from List_Of_All_Domains import DOMAINS

base_url = "linkedunion.org"
results = DOMAINS
alive_domains = []
not_alive_domains = []
main_menu_not_found = []


def check_domain(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    response = requests.get(url, headers=headers)
    print(f"{url}: {response.status_code}")
    if response.status_code == 404:
        print(f"{url} returned a 404 error")
    elif response.status_code == 504:
        not_alive_domains.append(url)
    else:
        if "Main Menu" in response.text:
            alive_domains.append(url)
        else:
            print(f"{url} is not up: 'Main Menu' not found.")
            main_menu_not_found.append(url)
            assert False

# Set the maximum number of concurrent threads
max_threads = 20

start_time = time.time()

with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
    # Submit the tasks to the executor
    futures = [executor.submit(check_domain, f"https://{sub_app_name}.web.{base_url}") for sub_app_name in results]

    # Wait for the tasks to complete
    concurrent.futures.wait(futures)

end_time = time.time()
execution_time = end_time - start_time

# Write the results to a CSV file
with open("Check_Status_Code_All_Domains.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Alive Domains", "504 Domains"])
    for i in range(max(len(alive_domains), len(not_alive_domains))):
        if i < len(alive_domains):
            alive_domain = alive_domains[i]
        else:
            alive_domain = ""
        if i < len(not_alive_domains):
            not_alive_domain = not_alive_domains[i]
        else:
            not_alive_domain = ""
        writer.writerow([alive_domain, not_alive_domain])

print("Results written to Check_Status_Code_All_Domains.csv")
print(f"Execution time: {execution_time} seconds")
print(f"Main Menu Not Found Domains {main_menu_not_found}")
