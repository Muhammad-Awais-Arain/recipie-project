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

def test_Webview(test_setup):
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
    driver.find_element(By.NAME, 'main_navigation[0][title]').send_keys("Pytest Web View Automation")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[2]/div/div[1]/div[2]/div[1]/div/div/button//*[text()="Multiple News"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[2]/div/div[1]/div[2]/div[1]/div/div/div//*[text()="Web View"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_navigation_submit"]').click()
    print("Web View Menu Added")
    time.sleep(2)

    #SIDE MENU EVENT CLICK
    driver.find_element(By.XPATH, '//*[@id="kt_aside_menu"]/ul/li[3]/a//*[text()="Pytest Web View Automation"]').click()
    time.sleep(1)
    #Adding News
    driver.find_element(By.XPATH, '//*[@id="kt-content"]/div/div[1]/div[2]/div/div[1]/a/button').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_wrapper"]/div[4]/div/div[1]/div/form/div[1]/div[1]/div/input[1]').send_keys("News Automation")
    time.sleep(1)
    driver.execute_script("CKEDITOR.instances['editor1'].setData('Web View Automation by using Pytest Selenium')")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_wrapper"]/div[4]/div/div[1]/div/form/div[2]/div/div/div[2]/button').click()
    time.sleep(2)

    #Website
    driver.get(website)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="top"]/nav/div[2]/div[2]/div[2]/div[6]/ul/li/a').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="top"]/nav/div[2]/div[2]/div[2]/div[6]/ul/li/ul/div[1]/section/nav/a').click()
    time.sleep(1)
    ele = driver.find_element(By.XPATH, '//h2[text()="News Automation"]')
    actions = ActionChains(driver)
    actions.click(on_element=ele)
    actions.perform()
    time.sleep(1)

    #Backend for privacy change
    driver.get(backend)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_aside_menu"]/ul/li[3]/a//*[text()="Pytest Web View Automation"]').click()
    time.sleep(2)
    a = driver.find_element(By.XPATH, '//*[@id="kt_apps_user_list_datatable"]/table/tbody/tr/td[5]/span/div/button/i')
    a.click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[7]/a[1]').click()
    time.sleep(3)

    #Website
    driver.get(website)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="top"]/nav/div[2]/div[2]/div[2]/div[6]/ul/li/a').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="top"]/nav/div[2]/div[2]/div[2]/div[6]/ul/li/ul/div[1]/section/nav/a').click()
    time.sleep(1)

    #login
    driver.find_element(By.XPATH, '//*[@id="login-message-popup"]/div/div/div[2]/p/a[1]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="generalSearch"]').send_keys("henry@mailinator.com")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="login-modal"]/div/div/form/div/div[3]/div[3]/span/div/input').send_keys("henry")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="login-modal"]/div/div/form/div/div[3]/div[5]/button').click()
    time.sleep(6)
    driver.find_element(By.XPATH, '//*[@id="top"]/nav/div[2]/div[2]/div[2]/div[6]/ul/li/a').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="top"]/nav/div[2]/div[2]/div[2]/div[6]/ul/li/ul/div[1]/section/nav/a').click()
    time.sleep(1)
    ele = driver.find_element(By.XPATH, '//h2[text()="News Automation"]')
    actions = ActionChains(driver)
    actions.click(on_element=ele)
    actions.perform()
    time.sleep(1)



    #Backend
    driver.get(backend)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_aside_menu"]/ul/li[3]/a//*[text()="Pytest Web View Automation"]').click()
    time.sleep(1)

    #status change
    driver.find_element(By.XPATH, '//*[@id="kt_apps_user_list_datatable"]/table/tbody/tr/td[6]/span/div/button').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[7]/a[2]').click()
    time.sleep(1)

    #Website
    driver.get(website)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="top"]/nav/div[2]/div[2]/div[2]/div[6]/ul/li/a').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="top"]/nav/div[2]/div[2]/div[2]/div[6]/ul/li/ul/div[1]/section/nav/a').click()
    time.sleep(1)

    # Backend
    driver.get(backend)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_aside_menu"]/ul/li[3]/a//*[text()="Pytest Web View Automation"]').click()
    time.sleep(1)
    #Edit
    driver.find_element(By.XPATH, '//*[@id="kt_apps_user_list_datatable"]/table/tbody/tr/td[8]/span/div/button').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[7]/ul/li[1]/a').click()
    time.sleep(1)
    driver.find_element(By.XPATH,'//*[@id="kt_wrapper"]/div[4]/div/div[1]/div/form/div[1]/div[1]/div/input[1]').clear()
    driver.find_element(By.XPATH, '//*[@id="kt_wrapper"]/div[4]/div/div[1]/div/form/div[1]/div[1]/div/input[1]').send_keys("Web View Automation")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_wrapper"]/div[4]/div/div[1]/div/form/div[1]/div[6]/div/div/div/span[3]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_wrapper"]/div[4]/div/div[1]/div/form/div[2]/div/div/div[2]/button').click()
    time.sleep(1)

    #Delete
    driver.find_element(By.XPATH, '//*[@id="kt_apps_user_list_datatable"]/table/tbody/tr/td[8]/span/div/button').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="delete"]/span').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[7]/div/div[3]/button[1]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[7]/div/div[3]/button[1]').click()
    time.sleep(1)
    #navigation delete
    driver.find_element(By.XPATH, '//*[@id="kt_header"]/div[2]/div[5]/div[1]/div/div/div[1]/a').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_header"]/div[2]/div[5]/div[2]/div[2]/a[4]/div[2]/div[1]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[1]/div[2]/div/a/i').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_navigation_submit"]').click()
    time.sleep(1)
    print("Tested Completed")
