from selenium import webdriver
import time
from List_Of_All_Domains import *
from selenium.webdriver.chrome.service import Service
import csv

# Extract the base URL from your app's base URL
base_url = "linkedunion.info"


# create a new Service object for the Chrome WebDriver
service = Service('chromedriver.exe')

# create a new Chrome WebDriver instance using the Service object
driver = webdriver.Chrome(service=service)
driver.maximize_window()
results = DOMAINS[1:20]

# Loop through each app path and open it in a new tab
for i, result in enumerate(results):
    sub_app_name = result
    url = f"http://{sub_app_name}.web.{base_url}"
    driver.execute_script(f"window.open('{url}', '_blank')")
    print(f"Website No: {i + 1}, Sub App Name: {sub_app_name}")
    # time.sleep(2)  # Wait for 5 seconds for the website to load

# Wait for all the websites to load completely
time.sleep(10)


with open('Web_Three_All_Domains.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Website No", "Title", "URL", "Sub App Name"])
    for i, handle in enumerate(driver.window_handles):
        driver.switch_to.window(handle)
        url = driver.current_url
        if ".web.linkedunion.info" in url:
            sub_app_name = url.split('.web.linkedunion.info')[0].split('//')[1]
            if "Application error" in driver.page_source:
                row = [i+1, "Application error", url, sub_app_name]
            else:
                row = [i+1, driver.title, url, sub_app_name]
        else:
            row = [i+1, driver.title, url, ""]
        writer.writerow(row)

print("Results written to Web_Three_All_Domains.csv")
