import requests
import threading

url = "https://pffi.web.linkedunion.org"

def make_request():
    response = requests.get(url)
    print(response.status_code)

threads = []
num_requests = 1000

for i in range(num_requests):
    t = threading.Thread(target=make_request)
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()
