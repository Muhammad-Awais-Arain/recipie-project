from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pytest, time, sys, re, os
from selenium import webdriver
from LoremIpsum import *


# driver.request_interceptor = lambda request: print(request.url)
backend = 'https://desibook.admin.linkedunion.org/'
website = 'http://desibook.web.linkedunion.org/'

wait = None
actions = None

def initialize_driver(url):
    global wait, actions

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    wait = WebDriverWait(driver, 20)
    actions = ActionChains(driver)

    return driver


def backend_login(driver):
    global wait
    email = 'luautomatedguru@linkedunion.com'
    password = 'Automation@1234'
    code = "345876"
    time.sleep(2)
    wait.until(EC.visibility_of_element_located((By.NAME, 'email')))
    driver.find_element(By.NAME, 'email').send_keys(email)

    wait.until(EC.visibility_of_element_located((By.NAME, 'password')))
    driver.find_element(By.NAME, 'password').send_keys(password)

    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kt_login_signin_submit"]'))).click()
    time.sleep(3)

    input_fields = driver.find_elements(By.CSS_SELECTOR, 'input[name="letters[]"]')

    for index, field in enumerate(input_fields):
        if index < len(code):
            field.send_keys(code[index])

    wait.until(EC.element_to_be_clickable((By.ID, 'kt_verify_two_factor_code'))).click()
    print("Login Successful")


def click_dropdown(dropdown_class_name):
    global wait
    dropdown_element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, dropdown_class_name)))
    dropdown_element.click()


def add_menu_item_and_navigate(title_text, select_option, URL, driver):
    # Check if the navigation already exists
    # side_elements = driver.find_elements(By.XPATH, f"//a[starts-with(@href, '/{URL}/{title_text.lower().replace(' ', '-')}/')]")
    # if len(side_elements) > 0:
    #     print("Navigation already exists.")
    # else:
    
    # MENU ADD
    global wait
    click_dropdown("kt-user-card-v2__name")
    user_menu_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/navigation/"]')))
    user_menu_element.click()
    driver.find_element(By.XPATH, '//*[@id="kt_navigation_form"]/div/div/div[1]/div[2]/div/div/a/span').click()
    driver.find_element(By.XPATH, '//*[@id="kt_navigation_submit"]').click()
    time.sleep(7)
    # driver.find_element(By.CSS_SELECTOR, '#kt_navigation_form > div > div > div:nth-child(1) > div:nth-child(2) > div > div > a > span').click()
    time.sleep(1)
    # CHANGING MENU NAME
    elements = wait.until(EC.presence_of_all_elements_located((By.ID, "kt_portlet_tools_4")))

    # get the last element in the list
    last_element = elements[-1]
    last_element.click()
    time.sleep(2)

    elements = driver.find_elements(By.CSS_SELECTOR, "input[name*='main_navigation'][name$='[title]']")

    # get the length of the list
    n = len(elements)

    # find the last element and click on it
    if n > 0:
        title = elements[-1]
        title.clear()
        title.send_keys(title_text)
    else:
        # handle the case where there are no elements
        print("No elements found")

    elements = driver.find_elements(By.CSS_SELECTOR, "select[name$='[action]']")

    # get the length of the list
    n = len(elements)

    # find the last element and click on it
    if n > 0:
        action_selectpicker = elements[-1]
        select = Select(action_selectpicker)
        select.select_by_visible_text(select_option)
    else:
        # handle the case where there are no elements
        print("No elements found")

    time.sleep(1)

    save_button = wait.until(EC.presence_of_element_located((By.ID, "kt_navigation_submit")))
    # move to the element
    actions = ActionChains(driver)
    actions.move_to_element(save_button).perform()
    # click the element
    save_button.click()
    time.sleep(8)
    # SIDE MENU EVENT CLICK
    side_element = driver.find_element(By.XPATH, f"//a[starts-with(@href, '/{URL}/{title_text.lower().replace(' ', '-')}/')]")
    # Scroll to the element
    driver.execute_script("arguments[0].scrollIntoView();", side_element)
    # Click the element
    side_element.click()
    time.sleep(2)


def select_dropdown_option(dropdown_class, option_value, driver):
    global wait
    select_element = driver.find_element(By.CLASS_NAME, dropdown_class)
    select = Select(select_element)
    select.select_by_value(option_value)


def click_element_by_partial_url(partial_url, driver):
    global wait
    driver.execute_script(f"window.open('{website}');")
    driver.switch_to.window(driver.window_handles[-1])

    # Wait for the element with text 'Main Menu' and click it
    Menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(), 'Main')]")))
    Menu.click()
    # Wait for the element with the provided partial URL and click it
    ClickMenu = wait.until(EC.element_to_be_clickable((By.XPATH, f"//a[contains(@href, '{partial_url}')]")))
    ClickMenu.click()


if __name__ == '__main__':
    pytest.main(["-v"])
