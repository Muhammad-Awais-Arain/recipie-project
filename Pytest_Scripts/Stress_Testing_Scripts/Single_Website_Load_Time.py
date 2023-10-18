from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

# Specify the URL to open multiple times
url = "https://desibook.web.linkedunion.org/"

execution_path = "chromedriver.exe"

# create a new Service object for the Chrome WebDriver
service = Service(execution_path)


# create a new Chrome WebDriver instance using the Service object
driver = webdriver.Chrome(service=service)
driver.get(url)
driver.maximize_window()
wait = WebDriverWait(driver, 10)

# Specify the number of times to open the website
num_times = 100

with open('Single_Website_load_time.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Website No", "Title", "URL", "Load Time (seconds)"])

    for i in range(num_times):
        start_time = time.time()

        driver.execute_script(f"window.open('{url}', '_blank')")

        # Wait until the new window is opened and switch to it
        wait.until(EC.number_of_windows_to_be(i + 2))
        driver.switch_to.window(driver.window_handles[i + 1])

        # Wait until the document.readyState is "complete"
        wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

        url = driver.current_url
        end_time = time.time()
        load_time = end_time - start_time
        row = [i+1, driver.title, url, load_time]
        writer.writerow(row)
        print(f"Website No: {i + 1}, Load Time: {load_time} seconds")

print("Results written to Single_Website_load_time.csv")
