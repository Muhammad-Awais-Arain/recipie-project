from selenium import webdriver
import time
from List_Of_All_Domains import *
from selenium.webdriver.chrome.service import Service
import csv
from datetime import datetime

# Extract the base URL from your app's base URL
base_url = "linkedunion.com"
#base_url = "linkedunion.org"
# create a new Service object for the Chrome WebDriver
service = Service('chromedriver.exe')

# create a new Chrome WebDriver instance using the Service object
driver = webdriver.Chrome(service=service)
driver.maximize_window()
results = DOMAINS[1:200]

# Record the start time
start_time = datetime.now()

# Loop through each app path and open it in a new tab
for i, result in enumerate(results):
    sub_app_name = result
    url = f"http://{sub_app_name}.web.{base_url}"
    driver.execute_script(f"window.open('{url}', '_blank')")
    print(f"Website No: {i + 1}, Sub App Name: {sub_app_name}")
    # time.sleep(2)  # Wait for 5 seconds for the website to load

# Wait for all the websites to load completely

end_time = datetime.now()



# calculate the difference between start and end times
duration = end_time - start_time
print(f"Script started at: {start_time}")
print(f"Script finished at: {end_time}")
print(f"Total time taken by loop to execute all domains: {duration}")

time.sleep(10)
with open('Web_Two_All_Domains.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Website No", "Title", "URL", "Sub App Name"])
    for i, handle in enumerate(driver.window_handles):
        driver.switch_to.window(handle)
        url = driver.current_url
        if ".web.linkedunion.com" in url:
            sub_app_name = url.split('.web.linkedunion.com')[0].split('//')[1]
            row = [i+1, driver.title, url, sub_app_name]
        else:
            row = [i+1, driver.title, url, ""]
        writer.writerow(row)



print("Results written to Web_Two_All_Domains.csv")

