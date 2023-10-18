import mysql.connector
from selenium import webdriver
import time

# Connect to your database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="linkedunion_migration"
)

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

# Define the SQL query to fetch the app paths
sql_query = "SELECT app_path FROM constant"

# Execute the query and fetch the results
mycursor.execute(sql_query)
results = mycursor.fetchall()

# Extract the base URL from your app's base URL
base_url = "linkedunion.org"

# Set up the Selenium webdriver
driver = webdriver.Chrome()
driver.maximize_window()

# Loop through each app path and open it in a new tab
for i, result in enumerate(results):
    app_path = result[0]
    sub_app_name = app_path.split("/")[-1]
    url = f"https://{sub_app_name}.web.{base_url}"
    driver.execute_script(f"window.open('{url}', '_blank')")
    print('Website No: ', i+1)
    # time.sleep(2)  # Wait for 5 seconds for the website to load

# Wait for all the websites to load completely
time.sleep(5)

# Switch to each tab and print the page title
for i, handle in enumerate(driver.window_handles):
    driver.switch_to.window(handle)
    print(f"Title of website {i+1}: {driver.title}")

# Keep the driver open
