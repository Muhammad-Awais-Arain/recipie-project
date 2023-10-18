import sys
import time
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import re
from selenium.webdriver.support.ui import Select
import os
import json


driver = webdriver.Chrome()
# driver.request_interceptor = lambda request: print(request.url)
backend = 'https://desibook.admin.linkedunion.org/'
wait = WebDriverWait(driver, 10)
actions = ActionChains(driver)


@pytest.fixture()
def test_BackendUserDetails():
    backend_user_details = {
        'email': 'luautomatedguru@linkedunion.com',
        'password': 'Automation@1234',
    }
    return backend_user_details


@pytest.fixture()
def test_setup(test_BackendUserDetails):

    driver.implicitly_wait(10)
    driver.maximize_window()
    actions = ActionChains(driver)
    driver.get(backend)
    backend_login(test_BackendUserDetails['email'], test_BackendUserDetails['password'])
    time.sleep(2)
    click_dropdown("kt-user-card-v2__name")


def backend_login(email, password):
    driver.find_element(By.NAME, 'email').send_keys(email)
    driver.find_element(By.NAME, 'password').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="kt_login_signin_submit"]').click()
    time.sleep(2)

    code = "345876"
    input_fields = driver.find_elements(By.CSS_SELECTOR, 'input[name="letters[]"]')

    for index, field in enumerate(input_fields):
        if index < len(code):
            field.send_keys(code[index])

    driver.find_element(By.ID, 'kt_verify_two_factor_code').click()
    print("Login Successful")


def click_dropdown(dropdown_class_name):
    dropdown_element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, dropdown_class_name)))
    dropdown_element.click()


def test_Create_Backend(test_setup):
    user_menu_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/union-onboarding/"]')))
    user_menu_element.click()
    run_backend_creation()


def upload_image(image_filename, image_xpath):
    # Find the file input element
    file_input = driver.find_element(By.NAME, image_xpath)

    # Get the current working directory
    current_dir = os.getcwd()

    # Construct the full image path
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(os.path.dirname(script_dir))
    image_folder = os.path.join(project_dir, "Pytest_Scripts", "Static", "Backend_Assets")
    image_path = os.path.join(image_folder, image_filename)
    print(image_path)
    # Check if the image file exists
    if not os.path.exists(image_path):
        print(f"Image file not found: {image_path}")
        return

    # Set the file path of the image to upload
    file_input.send_keys(image_path)
    # # Print a message to indicate the image upload
    # print(f"Image uploaded: {image_filename} (XPath: {image_xpath})")
    # print("image_filename:", image_filename)
    # print("image_xpath:", image_xpath)
    # print("image_folder:", image_folder)
    # print("image_path:", image_path)


def turn_off_toggle(toggle_label_text):
    toggle_labels = driver.find_elements(By.XPATH, f"//label[contains(text(), '{toggle_label_text}')]")
    for toggle_label in toggle_labels:
        toggle = toggle_label.find_element(By.XPATH, "./following-sibling::div[contains(@class, 'bootstrap-switch')]")
        if "bootstrap-switch-on" in toggle.get_attribute("class"):
            toggle.click()


def turn_on_toggle(toggle_label_text):
    toggle_labels = driver.find_elements(By.XPATH, f"//label[contains(text(), '{toggle_label_text}')]")
    for toggle_label in toggle_labels:
        toggle_switch = toggle_label.find_element(By.XPATH, "..//input[@type='checkbox']")
        if not toggle_switch.is_selected():
            toggle_switch.click()


def select_option_by_text(select_id, option_text):
    select_element = driver.find_element(By.ID, select_id)
    select = Select(select_element)
    select.select_by_visible_text(option_text)


def run_backend_creation():
    # with open('backend_data.json', 'r') as json_file:             ####THIS IS FOR THE JSON FILE IMPORT
    #     data = json.load(json_file)
    # backends = data['backends']
    num_runs = 1
    backend_json = generate_backend_json(num_runs)
    backends = json.loads(backend_json)['backends']

    for backend in backends:
        app_name = backend['app_name']
        website_link = backend['website_link']
        is_child_app = backend['is_child_app']
        images = backend['images']
        app_required = backend['app_required']
        website_required = backend['website_required']
        is_spanish_module_required = backend['is_spanish_module_required']
        theme = backend['theme']
        is_two_factor_auth_required = backend['is_two_factor_auth_required']
        app_type = backend['app_type']
        additional_notes = backend['additional_notes']

        new_backend = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/union-onboarding/new-backend/0/"]')))
        new_backend.click()
        
        app_name_element = wait.until(EC.element_to_be_clickable((By.ID, 'app_name')))
        app_name_element.send_keys(app_name)
        
        website_url = wait.until(EC.element_to_be_clickable((By.NAME, 'website_link')))
        website_url.send_keys(website_link)

        if is_child_app:
            turn_on_toggle("Is this child App?")

            # Wait for the parent app dropdown to become visible
            parent_app_dropdown = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "parent_app_id_dropdown")))

            # Select "PFFI" from the dropdown
            parent_app_select = Select(driver.find_element(By.CLASS_NAME, "parent_app_id"))
            parent_app_select.select_by_value("1")  # Assuming the value for "PFFI" is "1"

        for image in images:
            filename = image['filename']
            element_id = image['element_id']
            upload_image(filename, element_id)
        
        if not app_required:
            turn_off_toggle("Is the app required?")
        
        if not website_required:
            turn_off_toggle("Is the website required?")

        if is_spanish_module_required:
            yes_radio_button = driver.find_element(By.XPATH, '//*[@id="new_backend_form"]/div[5]/div/div/div/div[2]/div[1]/div[2]/label/span')
            yes_radio_button.click()

        if theme == 1:
            theme1_radio_button = driver.find_element(By.XPATH, '//*[@id="new_backend_form"]/div[5]/div/div/div/div[2]/div[2]/div[2]/label/span')
            theme1_radio_button.click()

        if not is_two_factor_auth_required:
            no_radio_button = driver.find_element(By.XPATH, '//*[@id="new_backend_form"]/div[5]/div/div/div/div[2]/div[3]/div[3]/label/span')
            no_radio_button.click()

        select_id = "kt_select2"
        select_option_by_text(select_id, app_type)
        
        enter_additional_notes(additional_notes)
        submit = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'submit')))
        submit.click()
        time.sleep(2)
        driver.save_screenshot("page_screenshot.png")
    # Assume you have obtained the current URL from the browser
    current_url = driver.current_url

    # Define the expected URL ending
    expected_url_ending = "/union-onboarding/"

    assert current_url.endswith(expected_url_ending), f"URL assertion failed. Expected ending: {expected_url_ending}, Actual URL: {current_url}"


def enter_additional_notes(notes):
    notes_textarea = driver.find_element(By.NAME, "additional_notes")
    notes_textarea.send_keys(notes)


def generate_backend_json(num_backends):
    backends = []

    for i in range(1, num_backends + 1):
        backend = {
            "app_name": f"Backend Automaton {i}",
            "website_link": "https://pffi.com",
            "is_child_app": False,
            "images": [
                {"filename": "App_Logo.svg", "element_id": "app_logo"},
                {"filename": "Top_Logo_With_Black_Text.svg", "element_id": "top_logo_with_black_text"},
                {"filename": "Login_Logo.svg", "element_id": "login_logo"},
                {"filename": "Favicon.ico", "element_id": "favicon"},
                {"filename": "Newsletter_Logo.png", "element_id": "newsletter_logo"}
            ],
            "app_required": False,
            "website_required": False,
            "is_spanish_module_required": False,
            "theme": 2,
            "is_two_factor_auth_required": False,
            "app_type": "OTHER TRADES",
            "additional_notes": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        }
        backends.append(backend)

    data = {"backends": backends}
    return json.dumps(data, indent=4)
