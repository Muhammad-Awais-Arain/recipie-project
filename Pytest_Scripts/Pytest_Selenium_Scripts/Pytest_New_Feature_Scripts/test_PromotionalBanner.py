import sys
import time

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture()
def test_setup():
    global driver
    # WebDriver Path for System
    if sys.platform == ('win32'):
        driver = webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")
    elif sys.platform == ('linux'):
        driver = webdriver.Chrome("~/Drivers/Google/Chrome/chromedriver_linux64")
    elif sys.platform == ('darwin'):
        driver = webdriver.Chrome(executable_path="/Users/avialdosolutions/Desktop/chromedriver")
    else:
        print("Are you sure you have the Selenium Webdriver installed in the correct path?")

    driver.implicitly_wait(10)
    driver.maximize_window()

def test_PromotionalBanner(test_setup):
    backend = 'https://wnylabortoday.admin.linkedunion.org/'
    website = 'https://wnylabortoday.web.linkedunion.org/'
    a = ActionChains(driver)
    driver.get(backend)
    time.sleep(1)
    driver.find_element(By.NAME, 'email').send_keys("sundus@linkedunion.com")
    time.sleep(1)
    driver.find_element(By.NAME, 'password').send_keys("123")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_login_signin_submit"]').click()
    time.sleep(1)
    print("Login Sucessfull")
    time.sleep(1)

    #Selecting Project Settings
    driver.find_element(By.XPATH, '//*[@id="kt_subheader"]/div/div/div/div[2]/a').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="kt_wizard_v4"]/div[1]/div/div[5]/div/div[2]/div').click()
    time.sleep(2)
    #driver.execute_script('document.getElementById("banner_details").scrollIntoView();')
    driver.find_element(By.XPATH, '//*[@id="kt_portlet_base_demo_1_1_tab_content"]/div/div[8]/div[12]/div/div/div/span[3]').click()
    time.sleep(2)
    driver.execute_script("CKEDITOR.instances['editor4'].setData('Not More than 60 words')")
    time.sleep(2)
    driver.find_element(By.ID, 'cke_373').click()
    time.sleep(3)
    driver.execute_script("$('.cke_dialog_ui_input_text:nth-child(1)').val('www.google.com')")
    time.sleep(1)
    driver.execute_script("$('.cke_dialog_ui_input_text').first().val('')")
    time.sleep(1)
    driver.execute_script("$('.cke_dialog_ui_input_text').first().val('Google')")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="cke_1070_label"]').click()
    time.sleep(1)

    driver.find_element(By.XPATH,'//*[@id="kt_form"]/div[7]/button[3]').click()
    time.sleep(1)
