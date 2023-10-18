import time
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

# create a new Service object for the Chrome WebDriver
service = Service('chromedriver.exe')

# create a new Chrome WebDriver instance using the Service object
driver = webdriver.Chrome(service=service)
backend = 'https://desibook.staging.linkedunion.org/'
website = 'http://desibook.web.linkedunion.org/'
wait = WebDriverWait(driver, 10)
actions = ActionChains(driver)


def login(email, password):
    driver.get(backend)
    driver.maximize_window()
    driver.find_element(By.NAME, 'email').send_keys(email)
    driver.find_element(By.NAME, 'password').send_keys(password)
    time.sleep(1)
    driver.find_element(By.ID, 'kt_login_signin_submit').click()
    time.sleep(2)
    try:
        twoFApopUp = wait.until(EC.element_to_be_clickable((By.ID, 'enable_twofa')))
        twoFApopUp.click()
    except TimeoutException:
        pass
    # 2FA WORK 
    if '/two-factor-authentication/' in driver.current_url:
        locator = (By.ID, "kt_verify_two_factor_code")
        # Wait until the button is not clickable
        wait.until_not(EC.element_to_be_clickable(locator))
    else:
        print("2FA not required")


def logout():
    NameDropdown = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "kt-user-card-v2__name")))
    NameDropdown.click()
    time.sleep(1)
    logout = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/signout"]')))
    logout.click()


def unblock_user(user_name):
    # Selecting User Management
    SubmitWeb = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "kt-user-card-v2__name")))
    SubmitWeb.click()
    user_menu_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/user-management/"]')))
    user_menu_element.click()
    time.sleep(1)
    driver.find_element(By.ID, 'generalSearch').send_keys(user_name)
    time.sleep(2)
    # Unblock User
    button = driver.find_element(By.CLASS_NAME, 'btn-icon-md')
    button.click()
    driver.find_element(By.ID, 'unblock').click()
    unblock = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "swal2-confirm")))
    unblock.click()
    time.sleep(1)
    Click_Ok = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "swal2-confirm")))
    Click_Ok.click()


def test_login():
    # Login as "awais@linkedunion.com"
    login("awais@linkedunion.com", "11111")
    n = 4
    for i in range(n):
        print(f"Iteration {i + 1}")
        driver.find_element(By.ID, 'kt_login_signin_submit').click()
        time.sleep(1)
    # Login as "mubashir@linkedunion.com"
    login("mubashir@linkedunion.com", "mubashir123")
    unblock_user("Awais")
    logout()
    # Login with correct credentials
    login("awais@linkedunion.com", "Awais@1234")
    print("Login Sucessfull")
    logout()

