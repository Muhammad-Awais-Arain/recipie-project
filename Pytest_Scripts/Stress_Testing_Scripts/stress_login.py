import csv
import threading
import requests
import time
from global_variable import dynamic_url
api_url = dynamic_url

app_id = 118
# Replace with the actual URL
BASE_URL = f'{api_url}/rest_api/login?app_id={app_id}&language=en'

# Number of requests per user
NUM_REQUESTS_PER_USER = 5

# Dictionary to track the requests for each user
requests_executed = {}

successful_logins = []
unsuccessful_logins = []

# Lock for thread-safe access to lists
lock = threading.Lock()
start_time = time.time()

# Function to perform login requests
def login_request(email, password):
    requests_executed[email] = 0
    for _ in range(NUM_REQUESTS_PER_USER):
        response = requests.post(
            BASE_URL,
            headers={
                'accept': 'application/json',
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            data={
                'email': email,
                'password': password
            }
        )
        requests_executed[email] += 1
        data = response.json()
        try:
            if 'developer_message' in data:
                with lock:
                    if data['status'] == 1:
                        if email not in successful_logins:
                            successful_logins.append(email)
                            print(f"User {email}: Successful Login - Developer Message: {data['developer_message']}")
                    else:
                        if email not in unsuccessful_logins:
                            unsuccessful_logins.append(email)
                            print(f"User {email}: Unsuccessful Login - Developer Message: {data['developer_message']}")
        except ValueError:
            print(f"User {email}: Non-JSON response - Status: {data.get('status', 'Unknown')}")

        # print(f"User {email}: Status - {data['status']}")

# Read data from users.csv and start threads
threads = []
with open('users.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        email = row['email']
        password = row['password']
        thread = threading.Thread(target=login_request, args=(email, password))
        threads.append(thread)
        thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

end_time = time.time()

total_time = end_time - start_time

print("Summary:")
for email, count in requests_executed.items():
    print(f"User {email} executed {count} requests.")
with lock:
    print(f"Successful Login: {successful_logins}")
    print(f"Unsuccessful Login: {unsuccessful_logins}")
total_requests = sum(count for count in requests_executed.values())
# Print the total number of requests
print("Total Requests Sent:", total_requests)
print("Total Execution Time:", total_time, "seconds")
print("All login attempts completed.")
