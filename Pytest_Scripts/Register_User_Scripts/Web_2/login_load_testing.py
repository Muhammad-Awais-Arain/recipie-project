from selenium import webdriver
import time
import csv
import concurrent.futures
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


def login_and_verify(user_data):
    email, password = user_data["email"], user_data["password"]

    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)
    driver.get("https://desibook.web.linkedunion.live/")
    
    header = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Member Login')))
    header.click()
    time.sleep(2)
    email_field = driver.find_element(By.NAME, "email")
    password_field = driver.find_element(By.NAME, "password")
    login_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "Forms_web_btn_primary__xkauL")))
    email_field.send_keys(email)
    password_field.send_keys(password)
    time.sleep(1)
    login_button.click()

    time.sleep(2)
    try:
        success_text_element = driver.find_element(By.XPATH, "//div[contains(@class, 'MainNavbar_alert_text__Al2kw')]")
        success_text = success_text_element.text
        if "Login successful" in success_text:
            print(f"Login successful for {email}")
            return email
        elif "Invalid email or password" in success_text:
            print(f"Login failed for {email}")
            return {"email": email, "password": password}
        else:
            print(f"Unknown status for {email}: {success_text}")
            return {"email": email, "password": password}
    except NoSuchElementException:
        print(f"Error occurred for {email}: Element not found")
        return {"email": email, "password": password}
    except:
        print(f"Error occurred for {email}: Unknown error")
        return {"email": email, "password": password}
    finally:
        driver.quit()


csv_file = "user_details.csv"
user_data_list = []

with open(csv_file, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        user_data_list.append({
            "email": row["email"],
            "password": row["password"],
        })

# Perform logins concurrently
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(login_and_verify, user_data_list))

successful_logins = [result for result in results if isinstance(result, str)]
failed_logins = [result for result in results if isinstance(result, dict)]

print("Successful logins:")
for email in successful_logins:
    print(email)

print("\nFailed logins:")
for user in failed_logins:
    print(f"Email: {user['email']}, Password: {user['password']}")
