import time
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import re
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import random
from faker import Faker
import pyperclip
import csv
import os


service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=service)
# driver.request_interceptor = lambda request: print(request.url)  ##For getting URL of each page
backend = 'https://dev.admin.linkedunion.org/'
website = 'http://dev.web.linkedunion.info/'
wait = WebDriverWait(driver, 60)
actions = ActionChains(driver)
fake = Faker()
global code


@pytest.fixture()
def test_setup(test_BackendUserDetails):

    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(backend)
    driver.find_element(By.NAME, 'email').send_keys(test_BackendUserDetails['email'])
    driver.find_element(By.NAME, 'password').send_keys(test_BackendUserDetails['password'])
    driver.find_element(By.XPATH, '//*[@id="kt_login_signin_submit"]').click()
    time.sleep(3)
    if '/two-factor-authentication/' in driver.current_url:
        locator = (By.ID, "kt_verify_two_factor_code")
        # Wait until the button is not clickable
        wait.until_not(EC.element_to_be_clickable(locator))
    else:
        print("2FA not required")
    # Proceed with the code
    time.sleep(1)


@pytest.fixture()
def test_UserDetails():
    first_name = fake.first_name()
    last_name = fake.last_name()
    password = fake.password(length=10)
    phone_no = fake.phone_number()
    dob = fake.date_of_birth().strftime('%m/%d/%Y')
    employee_id = fake.random_int(min=100000, max=999999)
    ssn = fake.random_int(min=1000, max=9999)

    user_details = {
        'firstName': first_name,
        'lastName': last_name,
        'password': password,
        'phoneNo': phone_no,
        'DOB': dob,
        'employeeID': str(employee_id),
        'SSN': ssn
    }
    return user_details


@pytest.fixture()
def test_BackendUserDetails():
    backend_user_details = {
        'email': 'awais@linkedunion.com',
        'password': 'Awais@1234',
    }
    return backend_user_details


##Copy temp mail 
def get_temp_email():
    #GOTO TEMP-MAIL.ORG TO COPY THE EMAIL ADDRESS
    driver.execute_script("window.open('https://tempmailo.com/')")

    handles = driver.window_handles
    # Switch to the new tab
    driver.switch_to.window(handles[-1])
    time.sleep(1)
    #wait for the copy email button to be clickable 
    email = (By.XPATH, '//*[@id="apptmo"]/div/div[1]/div[1]/div/button')
    CopyEmail = wait.until(EC.element_to_be_clickable(email))
    CopyEmail.click()
    # retrieve the copied email from the clipboard using pyperclip
    copied_email = pyperclip.paste()
    time.sleep(1)
    print(copied_email)
    
    return copied_email


#Register user on web function
def register_user():
    #GOTO WEBSITE FOR REGISTERING A USER
    driver.execute_script(f"window.open('{website}');")

    handles = driver.window_handles
    # Switch to the new tab
    driver.switch_to.window(handles[-1])
    time.sleep(1)
    header = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Member Login')))
    header.click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[text()="Please Sign Up!"]').click()


#get verification code from the temp mail site
def get_verification_code():
    #Switch to Email Tab to Copy the code
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(4)

    RefreshEmail = (By.XPATH, '//*[text()="Refresh"]')
    RefreshEmailClick = wait.until(EC.element_to_be_clickable(RefreshEmail))
    RefreshEmailClick.click()
    codeEmail = (By.XPATH, '(//*[text()="Verification Code"])')
    codeEmailClick = wait.until(EC.presence_of_element_located(codeEmail))
    codeEmailClick.click()
    time.sleep(1)

    #IFRAME WORK STARTS FROM HERE
    iframe = driver.find_element(By.ID, 'fullmessage')
    driver.switch_to.frame(iframe)

    DivText = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[3]')
    VerificationCode = DivText.text
    print(VerificationCode)
    driver.switch_to.default_content()

    code = re.search(r'Use code instead (\d+)\.', VerificationCode).group(1)
    return code


#Enter verification code to web function 
def enter_verification_code(code):
    driver.switch_to.window(driver.window_handles[2])
    time.sleep(1)
    verification_code_inputs = driver.find_elements(By.CSS_SELECTOR, 'div.d-flex input.form-control')
    time.sleep(1)
    for i, digit in enumerate(code):
        verification_code_inputs[i].send_keys(digit)


#Verify user using magic link
def click_magic_link():
    #Switch to Email Tab to Copy the code
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(4)

    RefreshEmail = (By.XPATH, '//*[text()="Refresh"]')
    RefreshEmailClick = wait.until(EC.element_to_be_clickable(RefreshEmail))
    RefreshEmailClick.click()
    codeEmail = (By.XPATH, '(//*[text()="Verification Code"])')
    codeEmailClick = wait.until(EC.presence_of_element_located(codeEmail))
    codeEmailClick.click()
    time.sleep(1)

    #IFRAME WORK STARTS FROM HERE
    iframe = driver.find_element(By.ID, 'fullmessage')
    driver.switch_to.frame(iframe)
    # Find the button element using its XPath
    magicLinkButton = (By.XPATH, '//a[contains(text(), "Verify")]')
    magicLinkButtonClick = wait.until(EC.element_to_be_clickable(magicLinkButton))
    driver.execute_script("arguments[0].scrollIntoView();", magicLinkButtonClick)
    magicLinkButtonClick.click()
    driver.switch_to.default_content()
    time.sleep(4)
    driver.switch_to.window(driver.window_handles[-2])
    time.sleep(3)


#Condition of Toggles function
def toggle_settings(twoFactor, adminApproval, unrecognized=None):
    projectSetting = (By.LINK_TEXT, 'Project Settings')
    projectSettingClick = wait.until(EC.presence_of_element_located(projectSetting))
    projectSettingClick.click()
    stepTwo = (By.XPATH, '//*[@id="kt_wizard_v4"]/div[1]/div/div[2]/div/div[2]/div')
    stepTwoClick = wait.until(EC.presence_of_element_located(stepTwo))
    stepTwoClick.click()
    time.sleep(1)

    twoFactorToggle = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="kt_form"]/div[2]/div/div/div[4]/div[3]/div[1]/div/div')))
    adminApprovalToggle = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="kt_form"]/div[2]/div/div/div[4]/div[3]/div[3]/div/div')))
    
    if unrecognized:
        unrecognizedToggle = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="allow_request_unrecognized_member"]/div/div')))

    if twoFactor == "on" and "bootstrap-switch-off" in twoFactorToggle.get_attribute("class"):
        twoFactorToggle.click()
        time.sleep(2)
        print("2FA Toggle is on now")

    if twoFactor == "off" and "bootstrap-switch-on" in twoFactorToggle.get_attribute("class"):
        twoFactorToggle.click()
        time.sleep(2)
        print("2FA Toggle is off now")

    if adminApproval == "on" and "bootstrap-switch-off" in adminApprovalToggle.get_attribute("class"):
        adminApprovalToggle.click()
        time.sleep(2)
        print('Admin approval is on now')

    if adminApproval == "off" and "bootstrap-switch-on" in adminApprovalToggle.get_attribute("class"):
        adminApprovalToggle.click()
        time.sleep(2)
        print('Admin approval is off now')

    if unrecognized and unrecognized == "on" and "bootstrap-switch-off" in unrecognizedToggle.get_attribute("class"):
        hover = actions.move_to_element(unrecognizedToggle)
        hover.perform()
        unrecognizedToggle.click()
        time.sleep(2)
        print("Unrecognized Toggle is on now")

    if unrecognized and unrecognized == "off" and "bootstrap-switch-on" in unrecognizedToggle.get_attribute("class"):
        hover = actions.move_to_element(unrecognizedToggle)
        hover.perform()
        unrecognizedToggle.click()
        time.sleep(2)
        print("Unrecognized Toggle is off now")

    SavePS = driver.find_element(By.XPATH, '//*[@id="kt_form"]/div[7]/button[3]')
    SavePS.click()
    time.sleep(1)
    Ok = driver.find_element(By.XPATH, '/html/body/div[11]/div/div[3]/button[1]')
    Ok.click()


###Member approval function
def click_member_approval_with_firstname(firstname):
    driver.switch_to.window(driver.window_handles[0])
    Click_Ok = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "swal2-confirm")))
    Click_Ok.click()
    time.sleep(1)
    side = wait.until(EC.presence_of_element_located((By.ID, "kt_aside_toggler")))
    side.click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '.kt-aside__brand-logo').click()
    MemberApproval = driver.find_element(By.CSS_SELECTOR, 'a[href="/union-members/member-approval/"]')
    MemberApproval.click()
    time.sleep(1)
    driver.find_element(By.ID, 'generalSearch').send_keys(firstname)
    time.sleep(1)
    dropDown = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "btn-icon-md")))
    dropDown.click()
    Accept = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "table_accept_button")))
    Accept.click()
    AcceptPopUp = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "swal2-confirm")))
    AcceptPopUp.click()


###Login to web function
def login_with_email_and_password(email, password):
    time.sleep(1)
    header = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Member Login')))
    header.click()
    time.sleep(1)
    driver.find_element(By.NAME, 'email').send_keys(email)
    driver.find_element(By.NAME, 'password').send_keys(password)
    time.sleep(1)
    LoginBtn = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "Forms_web_btn_primary__IPULW")))
    LoginBtn.click()


def add_member(firstName, lastName, DOB, employeeID, SSN):
    header = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="#"]')))
    header.click()
    user_menu_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/union-members/"]')))
    user_menu_element.click()
    dropDown = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn-icon-md')))
    dropDown.click()
    ADD = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/union-members/add/"]')))
    ADD.click()
    driver.find_element(By.NAME, 'first_name').send_keys(firstName)
    driver.find_element(By.NAME, 'last_name').send_keys(lastName)
    driver.execute_script(f'$("#kt_datepicker_1").val("{DOB}")')
    driver.find_element(By.NAME, 'employeeID').send_keys(employeeID)
    driver.find_element(By.NAME, 'socialSecurityNumber').send_keys(SSN)

    time.sleep(1)
    Submit = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "submit")))
    Submit.click()


###Save user details to CSV function
def save_user_details_to_csv(user_details, email):
    fieldnames = list(user_details.keys())
    fieldnames.append('email')
    file_exists = os.path.isfile('user_details.csv')
    with open('user_details.csv', 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        user_details['email'] = email
        writer.writerow(user_details)


if __name__ == '__main__':
    pytest.main(["-v"])
