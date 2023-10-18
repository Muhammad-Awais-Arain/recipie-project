from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
import csv

# Specify the URL to open multiple times
url = "https://desibook.web.linkedunion.org"

# create a new Service object for the Chrome WebDriver
service = Service('chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument('--headless')

# create a new Chrome WebDriver instance using the Service object
driver = webdriver.Chrome(service=service)
driver.get(url)
driver.maximize_window()

# Specify the number of times to open the website
num_times = 50

for i in range(num_times):
    driver.execute_script(f"window.open('{url}', '_blank')")
    print(f"Website No: {i + 1}")

# Wait for all the websites to load completely
time.sleep(10)

with open('Signle_Domain.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Website No", "Title", "URL"])
    for i, handle in enumerate(driver.window_handles):
        driver.switch_to.window(handle)
        url = driver.current_url
        row = [i+1, driver.title, url]
        writer.writerow(row)

print("Results written to Signle_Domain.csv")