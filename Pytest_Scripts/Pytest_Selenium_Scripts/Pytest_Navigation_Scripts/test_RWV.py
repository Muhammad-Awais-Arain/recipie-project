import sys
import time

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import os

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

def test_RWV(test_setup):
    backend = 'https://wnylabortoday.admin.linkedunion.org/'
    website = 'https://wnylabortoday.web.linkedunion.org/'
    a = ActionChains(driver)
    driver.get(backend)
    driver.find_element(By.NAME, 'email').send_keys("sundus@linkedunion.com")
    time.sleep(1)
    driver.find_element(By.NAME, 'password').send_keys("123")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_login_signin_submit"]').click()
    print("Login Sucessfull")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_header"]/div[2]/div[5]/div[1]/div/div/div[1]/a').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_header"]/div[2]/div[5]/div[2]/div[2]/a[4]/div[2]/div[1]').click()
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
    driver.find_element(By.NAME, 'main_navigation[0][title]').send_keys("Pytest Report Workplace Violation Automation")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[2]/div/div[1]/div[2]/div[1]/div/div/button//*[text()="Multiple News"]').click()
    driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[2]/div/div[1]/div[2]/div[1]/div/div/div//*[text()="Report Workplace Violation"]').click()
    driver.find_element(By.XPATH, '//*[@id="kt_navigation_submit"]').click()
    print("Report Workplace Violation Menu Added")
    time.sleep(2)

    # WEBSITE
    driver.get(website)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="top"]/nav/div[2]/div[2]/div[2]/div[6]/ul/li/a').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="top"]/nav/div[2]/div[2]/div[2]/div[6]/ul/li/ul/div[1]/section/nav/a').click()
    time.sleep(1)

    #Submitting form by User Name
    driver.find_element(By.XPATH, '//*[@id="main"]/section[2]/div[2]/div/div/div/form/div[2]/div[1]/div/span/input').send_keys("Henry Smith")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="main"]/section[2]/div[2]/div/div/div/form/div[2]/div[3]/div/span/input').send_keys("henry@mailinator.com")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="main"]/section[2]/div[2]/div/div/div/form/div[2]/div[5]/div/span/input').send_keys("Avialdo Solutions")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="main"]/section[2]/div[2]/div/div/div/form/div[2]/div[7]/div/span/input').send_keys("Karachi, Pakistan")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="main"]/section[2]/div[2]/div/div/div/form/div[2]/div[9]/div/span/input').send_keys("yes")
    time.sleep(1)

    driver.find_element(By.XPATH, '//*[@id="main"]/section[2]/div[2]/div/div/div/form/div[2]/div[2]/div/span/input').send_keys("12/21/2022")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="main"]/section[2]/div[2]/div/div/div/form/div[2]/div[4]/div/span/input').send_keys("12345567890")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="main"]/section[2]/div[2]/div/div/div/form/div[2]/div[6]/div/span/input').send_keys("1122")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="main"]/section[2]/div[2]/div/div/div/form/div[2]/div[8]/div/span/input').send_keys("Avialdo")
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="main"]/section[2]/div[2]/div/div/div/form/div[2]/div[10]/div/span/textarea').send_keys("I want Justice!")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight / 2)")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="main"]/section[2]/div[2]/div/div/div/form/div[2]/div[12]/div/input[1]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="main"]/section[2]/div[2]/div/div/div/form/div[2]/div[13]/div[1]/input[1]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="main"]/section[2]/div[2]/div/div/div/form/div[2]/div[13]/div[2]/input').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="main"]/section[2]/div[2]/div/div/div/form/div[4]/button').click()
    time.sleep(2)
    # Coming back to Backend again for checking form
    driver.get(backend)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_aside_menu"]/ul/li[3]/a//*[text()="Pytest Report Workplace Violation Automation"]').click()
    time.sleep(1)
    #View
    driver.find_element(By.XPATH, '//*[@id="kt_apps_user_list_datatable"]/table/tbody/tr/td[6]/span/div/button').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[text()="View"]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="kt-content"]/div/div[1]/div[2]/div/a').click()
    time.sleep(1)


    #Delete
    driver.find_element(By.XPATH, '//*[@id="kt_apps_user_list_datatable"]/table/tbody/tr/td[6]/span/div/button').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="delete"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[7]/div/div[3]/button[1]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[7]/div/div[3]/button[1]').click()
    time.sleep(1)
    #Navigation Delete
    driver.find_element(By.XPATH, '//*[@id="kt_header"]/div[2]/div[5]/div[1]/div/div/div[1]/a').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_header"]/div[2]/div[5]/div[2]/div[2]/a[4]/div[2]/div[1]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[1]/div[2]/div/a').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_navigation_submit"]').click()
    time.sleep(1)
    driver.quit()
