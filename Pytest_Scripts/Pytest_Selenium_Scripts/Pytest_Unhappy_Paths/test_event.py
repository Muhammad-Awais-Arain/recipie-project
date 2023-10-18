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

def test_addevent(test_setup):
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
    driver.find_element(By.XPATH, '//*[@id="kt_header"]/div[2]/div[6]/div[1]/div/div/div[1]/a').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_header"]/div[2]/div[6]/div[2]/div[2]/a[4]/div[2]/div[1]').click()
    time.sleep(1)
    #MENU ADD
    driver.find_element(By.XPATH, '//*[@id="kt_navigation_form"]/div/div/div[1]/div[2]/div/div/a/span').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_navigation_submit"]').click()
    time.sleep(1)
    #CHANGING MENU NAME
    driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[1]/div[1]//*[text()="New Menu"]').click()
    time.sleep(1)
    driver.find_element(By.NAME, 'main_navigation[0][title]').clear()
    time.sleep(1)
    driver.find_element(By.NAME, 'main_navigation[0][title]').send_keys("Pytest Failed Event Automation")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[2]/div/div[1]/div[2]/div[1]/div/div/button//*[text()="Multiple News"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[2]/div/div[1]/div[2]/div[1]/div/div/div//*[text()="Event"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_navigation_submit"]').click()
    time.sleep(1)

    print("Event Menu Added")
    time.sleep(2)
    #SIDE MENU EVENT CLICK
    driver.find_element(By.XPATH, '//*[@id="kt_aside_menu"]/ul/li[3]/a//*[text()="Pytest Failed Event Automation"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt-content"]/div/div[1]/div[2]/div/div[1]/a/button').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[1]/div[1]/div/input').send_keys("Event Automation Using Pytest Selenium whenever this script will be runned event will always give error becuase it does not accept more than 200 characters. Now lets see if it is accepting the title or not.")
    time.sleep(1)
    #START DATE
    driver.find_element(By.ID, 'kt_datetimepicker_3').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[8]/div[3]/table/tbody/tr[5]/td[4]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[8]/div[2]/table/tbody/tr/td/fieldset[2]/span[4]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[8]/div[1]/table/tbody/tr/td/fieldset/span[11]').click()
    time.sleep(1)

    #END DATE
    driver.find_element(By.ID, 'kt_datetimepicker_4').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[9]/div[3]/table/tbody/tr[6]/td[1]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[9]/div[2]/table/tbody/tr/td/fieldset[2]/span[12]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[9]/div[1]/table/tbody/tr/td/fieldset/span[12]').click()
    time.sleep(1)

    #LOCATION
    driver.find_element(By.XPATH, '//*[@id="address"]').send_keys('Karachi, Pakistan')
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[1]/div[6]/div/textarea').send_keys('Testing Automation')
    time.sleep(1)

    #Event Added Sucesfully
    driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[2]/div/div/div[2]/button').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[1]/div[1]/div/input').clear()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[1]/div[1]/div/input').send_keys("Event Automation Using Pytest Selenium")
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[2]/div/div/div[2]/button').click()
    time.sleep(3)
    driver.find_element(By.XPATH,'//*[@id="kt_apps_user_list_datatable"]/table/thead/tr/th[2]/span/label').click()
    time.sleep(2)

    #Delete
    driver.find_element(By.XPATH,'//*[@id="kt_subheader_group_actions_delete_all"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[7]/div/div[3]/button[1]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[7]/div/div[3]/button[1]').click()
    time.sleep(1)
    #Navigation Delete
    driver.find_element(By.XPATH, '//*[@id="kt_header"]/div[2]/div[6]/div[1]/div/div/div[1]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_header"]/div[2]/div[6]/div[2]/div[2]/a[4]/div[2]/div[1]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[1]/div[2]/div/a').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_navigation_submit"]').click()
    time.sleep(1)
    driver.execute_script('alert("Test Add Event executed Succesfully")')
    time.sleep(3)
    driver.quit()
    print("Automated Sucessfully")