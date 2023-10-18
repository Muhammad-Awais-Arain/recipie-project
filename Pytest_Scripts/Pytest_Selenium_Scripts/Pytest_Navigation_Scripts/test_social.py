import sys
import time
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By


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

def test_multiplenews(test_setup):
    backend = 'https://wnylabortoday.admin.linkedunion.org/'
    website = 'https://wnylabortoday.web.linkedunion.org/'

    driver.get(backend)
    driver.find_element(By.NAME, 'email').send_keys("sundus@linkedunion.com")
    driver.find_element(By.NAME, 'password').send_keys("123")
    driver.find_element(By.XPATH, '//*[@id="kt_login_signin_submit"]').click()
    print("Login Sucessfull")
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
    driver.find_element(By.NAME, 'main_navigation[0][title]').send_keys("Pytest Social Media Automation")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[2]/div/div[1]/div[2]/div[1]/div/div/button//*[text()="Multiple News"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[2]/div/div[1]/div[2]/div[1]/div/div/div//*[text()="Social Media"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_navigation_submit"]').click()
    print("Social Media Menu Added")
    time.sleep(2)

    #SIDE MENU EVENT CLICK
    driver.find_element(By.XPATH, '//*[@id="kt_aside_menu"]/ul/li[3]/a//*[text()="Pytest Social Media Automation"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt-content"]/div/div[1]/div[2]/div/div[1]/button[1]').click()
    time.sleep(3)
    driver.execute_script('document.getElementById("name").value="Facebook";')
    time.sleep(1)
    driver.find_element(By.ID, 'link').send_keys("https://www.facebook.com/")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="stay_connected_modal"]/div/div/div[3]/button[1]').click()
    time.sleep(2)

    #Checking on website
    driver.get(website)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="top"]/nav/div[2]/div[2]/div[2]/div[6]/ul/li/a').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="top"]/nav/div[2]/div[2]/div[2]/div[6]/ul/li/ul/div[1]/section/nav/a').click()
    time.sleep(1)


    #backend again for deleting
    driver.get(backend)
    driver.find_element(By.XPATH, '//*[@id="kt_aside_menu"]/ul/li[3]/a//*[text()="Pytest Social Media Automation"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_apps_user_list_datatable"]/table/tbody/tr/td[5]/span/div/button').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="delete"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[5]/div/div[3]/button[1]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[5]/div/div[3]/button[1]').click()
    time.sleep(1)

    #Deleting Menu
    driver.find_element(By.XPATH, '//*[@id="kt_header"]/div[2]/div[5]/div[1]/div/div/div[1]/a').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_header"]/div[2]/div[5]/div[2]/div[2]/a[4]/div[2]/div[1]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[1]/div[2]/div/a/i').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_navigation_submit"]').click()
    time.sleep(2)
    print("Social Media Menu Added")
    driver.execute_script("alert('Social Media Added!')")
    driver.quit()