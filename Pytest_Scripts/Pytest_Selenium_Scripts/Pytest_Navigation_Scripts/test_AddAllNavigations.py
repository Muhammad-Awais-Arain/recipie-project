from test_Menu import *

def test_AddAllNavigations(test_setup):
    Name_Dropdown()
    user_menu_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/navigation/"]')))
    user_menu_element.click()
    #MENU ADD
    time.sleep(1)
    driver.find_element(By.ID, 'add_menu_navigation').click()
    driver.find_element(By.ID, 'add_menu_navigation').click()
    driver.find_element(By.ID, 'add_menu_navigation').click()
    driver.find_element(By.ID, 'add_menu_navigation').click()
    driver.find_element(By.ID, 'add_menu_navigation').click()
    driver.find_element(By.ID, 'add_menu_navigation').click()
    driver.find_element(By.ID, 'add_menu_navigation').click()
    driver.find_element(By.ID, 'add_menu_navigation').click()
    driver.find_element(By.ID, 'add_menu_navigation').click()
    driver.find_element(By.ID, 'add_menu_navigation').click()
    driver.find_element(By.ID, 'add_menu_navigation').click()
    driver.find_element(By.ID, 'add_menu_navigation').click()
    driver.find_element(By.ID, 'add_menu_navigation').click()
    driver.find_element(By.ID, 'add_menu_navigation').click()
    driver.find_element(By.ID, 'add_menu_navigation').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_navigation_submit"]').click()
    time.sleep(2)
    #Event
    driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[1]/div[1]//*[text()="New Menu"]').click()
    driver.find_element(By.NAME, 'main_navigation[0][title]').clear()
    driver.find_element(By.NAME, 'main_navigation[0][title]').send_keys("Event Automation")
    driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[2]/div/div[1]/div[2]/div[1]/div/div/button//*[text()="Multiple News"]').click()
    driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[2]/div/div[1]/div[2]/div[1]/div/div/div//*[text()="Event"]').click()
    time.sleep(1)
    #Web View
    driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[1]/div[1]//*[text()="New Menu"]').click()
    driver.find_element(By.NAME, 'main_navigation[1][title]').clear()
    driver.find_element(By.NAME, 'main_navigation[1][title]').send_keys("Web Link Automation")
    driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[2]/div/div[1]/div[2]/div[1]/div/div/button//*[text()="Multiple News"]').click()
    driver.find_element(By.XPATH, '//*[@id="bs-select-17-8"]').click()
    time.sleep(1)
    #Report Workplace Violence
    driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[1]/div[1]//*[text()="New Menu"]').click()
    driver.find_element(By.NAME, 'main_navigation[2][title]').clear()
    driver.find_element(By.NAME, 'main_navigation[2][title]').send_keys("Report Workplace Violence Automation")
    driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[2]/div/div[1]/div[2]/div[1]/div/div/button//*[text()="Multiple News"]').click()
    driver.find_element(By.XPATH, '//*[@id="bs-select-18-5"]').click()
    time.sleep(1)
    #SBS
    driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[1]/div[1]//*[text()="New Menu"]').click()
    driver.find_element(By.NAME, 'main_navigation[3][title]').clear()
    driver.find_element(By.NAME, 'main_navigation[3][title]').send_keys("SBS Automation")
    driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[2]/div/div[1]/div[2]/div[1]/div/div/button//*[text()="Multiple News"]').click()
    driver.find_element(By.XPATH, '//*[@id="bs-select-19-16"]').click()
    time.sleep(1)
    #Social Media
    driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[1]/div[1]//*[text()="New Menu"]').click()
    driver.find_element(By.NAME, 'main_navigation[4][title]').clear()
    driver.find_element(By.NAME, 'main_navigation[4][title]').send_keys("Social Media Automation")
    driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[2]/div/div[1]/div[2]/div[1]/div/div/button//*[text()="Multiple News"]').click()
    driver.find_element(By.XPATH, '//*[@id="bs-select-20-2"]').click()
    time.sleep(1)
    #Union Representative
    driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[1]/div[1]//*[text()="New Menu"]').click()
    driver.find_element(By.NAME, 'main_navigation[5][title]').clear()
    driver.find_element(By.NAME, 'main_navigation[5][title]').send_keys("Union Representative Automation")
    driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[2]/div/div[1]/div[2]/div[1]/div/div/button//*[text()="Multiple News"]').click()
    driver.find_element(By.XPATH, '//*[@id="bs-select-21-7"]').click()
    time.sleep(1)
    #Multiple News
    driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[1]/div[1]//*[text()="New Menu"]').click()
    driver.find_element(By.NAME, 'main_navigation[6][title]').clear()
    driver.find_element(By.NAME, 'main_navigation[6][title]').send_keys("Multiple News Automation")
    time.sleep(1)
    #Find My Elected Officials
    driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[1]/div[1]//*[text()="New Menu"]').click()
    driver.find_element(By.NAME, 'main_navigation[7][title]').clear()
    driver.find_element(By.NAME, 'main_navigation[7][title]').send_keys("Find My Elected Officials Automation")
    driver.find_element(By.XPATH, '(//*[@id="kt_portlet_tools_4"]/div[2]/div/div[1]/div[2]/div[1]/div/div/button//*[text()="Multiple News"])[2]').click()
    driver.find_element(By.XPATH, '//*[@id="bs-select-23-3"]').click()
    time.sleep(1)
    #Organize my workplace
    driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[1]/div[1]//*[text()="New Menu"]').click()
    driver.find_element(By.NAME, 'main_navigation[8][title]').clear()
    driver.find_element(By.NAME, 'main_navigation[8][title]').send_keys("Organize My Workplace Automation")
    driver.find_element(By.XPATH, '(//*[@id="kt_portlet_tools_4"]/div[2]/div/div[1]/div[2]/div[1]/div/div/button//*[text()="Multiple News"])[2]').click()
    driver.find_element(By.XPATH, '//*[@id="bs-select-24-13"]').click()
    time.sleep(1)
    #Multiple Web Links
    driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[1]/div[1]//*[text()="New Menu"]').click()
    driver.find_element(By.NAME, 'main_navigation[9][title]').clear()
    driver.find_element(By.NAME, 'main_navigation[9][title]').send_keys("Multiple Web Links Automation")
    driver.find_element(By.XPATH, '(//*[@id="kt_portlet_tools_4"]/div[2]/div/div[1]/div[2]/div[1]/div/div/button//*[text()="Multiple News"])[2]').click()
    driver.find_element(By.XPATH, '//*[@id="bs-select-25-11"]').click()
    time.sleep(1)
    #Work Schedule
    driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[1]/div[1]//*[text()="New Menu"]').click()
    driver.find_element(By.NAME, 'main_navigation[10][title]').clear()
    driver.find_element(By.NAME, 'main_navigation[10][title]').send_keys("Work Schedule Automation")
    driver.find_element(By.XPATH, '(//*[@id="kt_portlet_tools_4"]/div[2]/div/div[1]/div[2]/div[1]/div/div/button//*[text()="Multiple News"])[2]').click()
    driver.find_element(By.XPATH, '//*[@id="bs-select-26-9"]').click()
    time.sleep(1)
    #Member Discount
    driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[1]/div[1]//*[text()="New Menu"]').click()
    driver.find_element(By.NAME, 'main_navigation[11][title]').clear()
    driver.find_element(By.NAME, 'main_navigation[11][title]').send_keys("Member Discount Automation")
    driver.find_element(By.XPATH, '(//*[@id="kt_portlet_tools_4"]/div[2]/div/div[1]/div[2]/div[1]/div/div/button//*[text()="Multiple News"])[2]').click()
    driver.find_element(By.XPATH, '//*[@id="bs-select-27-6"]').click()
    time.sleep(1)
    #Gallery
    driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[1]/div[1]//*[text()="New Menu"]').click()
    driver.find_element(By.NAME, 'main_navigation[12][title]').clear()
    driver.find_element(By.NAME, 'main_navigation[12][title]').send_keys("Gallery Automation")
    driver.find_element(By.XPATH, '(//*[@id="kt_portlet_tools_4"]/div[2]/div/div[1]/div[2]/div[1]/div/div/button//*[text()="Multiple News"])[2]').click()
    driver.find_element(By.XPATH, '//*[@id="bs-select-28-14"]').click()
    time.sleep(1)
    #Album
    driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[1]/div[1]//*[text()="New Menu"]').click()
    driver.find_element(By.NAME, 'main_navigation[13][title]').clear()
    driver.find_element(By.NAME, 'main_navigation[13][title]').send_keys("Album Automation")
    driver.find_element(By.XPATH, '(//*[@id="kt_portlet_tools_4"]/div[2]/div/div[1]/div[2]/div[1]/div/div/button//*[text()="Multiple News"])[2]').click()
    driver.find_element(By.XPATH, '//*[@id="bs-select-29-15"]').click()
    time.sleep(1)
    #Sub Menu
    driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[1]/div[1]//*[text()="New Menu"]').click()
    driver.find_element(By.NAME, 'main_navigation[14][title]').clear()
    driver.find_element(By.NAME, 'main_navigation[14][title]').send_keys("Sub Menu Automation")
    driver.find_element(By.XPATH, '(//*[@id="kt_portlet_tools_4"]/div[2]/div/div[1]/div[2]/div[1]/div/div/button//*[text()="Multiple News"])[2]').click()
    driver.find_element(By.XPATH, '//*[@id="bs-select-30-1"]').click()
    time.sleep(1)
    #Submit
    driver.execute_script("$(window).scrollTop(0);")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_navigation_submit"]').click()
    time.sleep(4)
    # driver.get(website)
    # time.sleep(2)
    # driver.find_element(By.XPATH, '//*[@id="top"]/nav/div[2]/div[2]/div[2]/div[6]/ul/li/a').click()
    # time.sleep(1)
    # driver.get(backend)
    # driver.find_element(By.XPATH, '//*[@id="kt_header"]/div[2]/div[6]/div[1]/div/div/div[1]/a').click()
    # time.sleep(1)
    # driver.find_element(By.XPATH, '//*[@id="kt_header"]/div[2]/div[6]/div[2]/div[2]/a[4]/div[2]/div[1]').click()
    # time.sleep(1)

    # #Deleting All navigations
    # driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[1]/div[2]/div/a').click()
    # time.sleep(1)
    # driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[1]/div[2]/div/a').click()
    # time.sleep(1)
    # driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[1]/div[2]/div/a').click()
    # time.sleep(1)
    # driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[1]/div[2]/div/a').click()
    # time.sleep(1)
    # driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[1]/div[2]/div/a').click()
    # time.sleep(1)
    # driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[1]/div[2]/div/a').click()
    # time.sleep(1)
    # driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[1]/div[2]/div/a').click()
    # time.sleep(1)
    # driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[1]/div[2]/div/a').click()
    # time.sleep(1)
    # driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[1]/div[2]/div/a').click()
    # time.sleep(1)
    # driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[1]/div[2]/div/a').click()
    # time.sleep(1)
    # driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[1]/div[2]/div/a').click()
    # time.sleep(1)
    # driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[1]/div[2]/div/a').click()
    # time.sleep(1)
    # driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[1]/div[2]/div/a').click()
    # time.sleep(1)
    # driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[1]/div[2]/div/a').click()
    # time.sleep(1)
    # driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[1]/div[2]/div/a').click()
    # time.sleep(1)
    # driver.find_element(By.ID, 'kt_navigation_submit').click()
    # print("all navigations added successfully")
    # driver.quit()
