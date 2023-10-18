import requests
import concurrent.futures
import time
import json
import sys
from website_test_links import DOMAINS

results = DOMAINS
alive_2_0_domains = []
alive_3_0_domains = []
not_alive_2_0_domains = []
not_alive_3_0_domains = []
missing_main_menu_domains = []
connection_errors = []
slow_domains = []


def check_domain(url):
    print(f"Checking domain: {url}")

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    try:
        # Separate timeout for connection errors (e.g., DNS resolution errors)
        response = requests.get(url, headers=headers, timeout=60)

        if response.status_code == 200:
            # If the request is successful, check for "Main Menu" in the response
            if "Main Menu" in response.text:
                # If "Main Menu" is found, check for "All Menus" to determine 3.0 websites
                if "All Menus" in response.text:
                    alive_3_0_domains.append(url)
                else:
                    alive_2_0_domains.append(url)
            else:
                missing_main_menu_domains.append(url)
        else:
            # If the website is down, check whether it is 2.0 or 3.0 based on response text
            if "Main Menu" in response.text:
                connection_errors.append((url, response.status_code))
            elif "All Menus" in response.text:
                connection_errors.append((url, response.status_code))
            else:
                connection_errors.append((url, None))  # Append the domain and None status code for connection errors

    except requests.exceptions.Timeout as e:
        # Timeout for connection errors (e.g., DNS resolution errors)
        connection_errors.append((url, None))  # Append the domain and None status code for connection errors
        print(f"Timeout error checking domain {url}: {str(e)}")
    except requests.exceptions.RequestException as e:
        # If there's any other request exception (e.g., connection refused), add to connection_errors
        connection_errors.append((url, None))  # Append the domain and None status code for connection errors
        print(f"Error checking domain {url}: {str(e)}")
    except Exception as e:
        # If there's any other exception, add to connection_errors
        connection_errors.append((url, None))  # Append the domain and None status code for connection errors
        print(f"Error checking domain {url}: {str(e)}")
    else:
        # If there was no exception, calculate the response time and check if it's slow
        response_time = response.elapsed.total_seconds()
        if response_time > 30:
            slow_domains.append((url, response_time))

# Set the maximum number of concurrent threads
max_threads = 20  # Increasing the max_threads value to 20
start_time = time.time()


with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
    # Submit the tasks to the executor
    futures = [executor.submit(check_domain, domain_url) for domain_url in results]

    # Wait for the tasks to complete
    concurrent.futures.wait(futures)

end_time = time.time()
execution_time = end_time - start_time

minutes = int(execution_time // 60)
seconds = int(round(execution_time % 60))

# Write log files
with open('2_0_alive_domains.log', 'w') as f:
    for domain in alive_2_0_domains:
        f.write(f"{domain}\n")

with open('3_0_alive_domains.log', 'w') as f:
    for domain in alive_3_0_domains:
        f.write(f"{domain}\n")

with open('missing_main_menu_domains.log', 'w') as f:
    for domain in missing_main_menu_domains:
        f.write(f"{domain}\n")

with open('connection_errors.log', 'w') as f:
    for domain, status_code in connection_errors:
        f.write(f"{domain}, Status Code: {status_code}\n")

with open('slow_domains.log', 'w') as f:
    for domain, response_time in slow_domains:
        f.write(f"{domain}, Response Time: {response_time} seconds\n")

print(f"Executed in {minutes} Minutes and {seconds} Seconds")
