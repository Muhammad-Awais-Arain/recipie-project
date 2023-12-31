from test_Menu import *
def test_SubMenu(test_setup):

    user_menu_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/navigation/"]')))
    user_menu_element.click()
    #MENU ADD
    driver.find_element(By.XPATH, '//*[@id="kt_navigation_form"]/div/div/div[1]/div[2]/div/div/a/span').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_navigation_submit"]').click()
    time.sleep(1)


    #CHANGING MENU NAME
    driver.find_element(By.XPATH, '//*[text()="New Menu"]').click()
    time.sleep(1)
    driver.find_element(By.NAME, 'main_navigation[14][title]').clear()
    time.sleep(1)
    driver.find_element(By.NAME, 'main_navigation[14][title]').send_keys("Pytest Sub Menu Automation")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[text()="Multiple News"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[text()="Sub Menu"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_navigation_submit"]').click()
    print("Sub Menu Added")

    #Adding Sub Menu
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[1]/div[1]//*[text()="Pytest Sub Menu Automation"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="inner-repeater"]/div[1]/div/div[2]/a').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '(//*[@id="kt_portlet_tools_4"]/div[1]/div[1])[2]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '(//*[@id="kt_portlet_tools_4"]/div[2]/div/div/div[1]/div[1]/div/div/div/input[1])[2]').send_keys("Social Media Sub Menu")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[2]/div/div[1]/div[2]/div[1]/div/div/button//*[text()="Multiple News"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[2]/div/div[1]/div[2]/div[1]/div/div/div//*[text()="Web Link"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_navigation_submit"]').click()
    time.sleep(2)
    # SIDE MENU EVENT CLICK

    driver.find_element(By.XPATH, '//*[@id="kt_aside_menu"]/ul/li[3]/a').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="kt_aside_menu"]/ul/li[3]/div/ul/li/a/span').click()
    time.sleep(1)

    #Adding Link
    driver.find_element(By.XPATH, '//*[@id="kt-content"]/div/div[1]/div[2]/div/div[1]/button').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="title"]').send_keys("LinkedUnion")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="link"]').send_keys("https://linkedunion.com/")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="web_link_modal"]/div/div/div[3]/button[1]').click()
    time.sleep(2)
    driver.get(website)
    driver.find_element(By.XPATH, '//*[@id="top"]/nav/div[2]/div[2]/div[2]/div[6]/ul/li/a').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="top"]/nav/div[2]/div[2]/div[2]/div[6]/ul/li/ul/div[1]/section/nav/a').click()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)
    driver.get(backend)

    # SIDE MENU EVENT CLICK
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_aside_menu"]/ul/li[3]/a').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="kt_aside_menu"]/ul/li[3]/div/ul/li/a/span').click()
    time.sleep(1)

    driver.find_element(By.XPATH, '//*[@id="kt_apps_user_list_datatable"]/table/tbody/tr/td[6]/span/div/button/i').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="delete"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[5]/div/div[3]/button[1]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[5]/div/div[3]/button[1]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_header"]/div[2]/div[5]/div[1]/div/div/div[1]/a').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_header"]/div[2]/div[5]/div[2]/div[2]/a[4]/div[2]/div[1]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[1]/div[2]/div/a/i').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_navigation_submit"]').click()
    time.sleep(1)
    print("Social Media Sub Menu Added")