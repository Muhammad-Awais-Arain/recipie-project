from test_Menu import *

def test_MltipleWebLinks(test_setup):

    add_menu_item_and_navigate("Pytest Multiple Web Links Automation", "Multiple Web Links", "web-link")

    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt-content"]/div/div[1]/div[2]/div/div[1]/button[1]').click()
    time.sleep(1)
    driver.find_element(By.XPATH,' //*[@id="title"]').send_keys("Facebook")
    driver.find_element(By.XPATH,' //*[@id="link"]').send_keys("https://www.facebook.com")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="web_link_modal"]/div/div/div[3]/button[1]').click()
    time.sleep(1)
    #website
    click_element_by_partial_url("/wufoo-form-multiple/pytest-multiple-web-links-automation/")

    driver.find_element(By.XPATH, '//*[@id="main"]/div/section/div/div/div/div[1]/div/div/div/a').click()
    time.sleep(4)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)
    
    #backend
    driver.find_element(By.XPATH, '//*[@id="kt_aside_menu"]/ul/li[3]/a//*[text()="Pytest Multiple Web Links Automation"]').click()
    time.sleep(1)
    #Edit
    driver.find_element(By.XPATH, '//*[@id="kt_apps_user_list_datatable"]/table/tbody/tr/td[6]/span/div/button').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[text()="Edit"]').click()
    time.sleep(2)
    driver.find_element(By.XPATH,' //*[@id="title"]').clear()
    driver.find_element(By.XPATH,' //*[@id="title"]').send_keys("LinkedIn")
    driver.find_element(By.XPATH,' //*[@id="link"]').clear()
    driver.find_element(By.XPATH,' //*[@id="link"]').send_keys("https://www.linkedin.com")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="web_link_modal"]/div/div/div[3]/button[1]').click()
    time.sleep(2)

    #History
    driver.find_element(By.XPATH, '//*[@id="kt_apps_user_list_datatable"]/table/tbody/tr/td[6]/span/div/button').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[text()="History"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="kt-content"]/div/div[1]/div[2]/div/a').click()
    time.sleep(1)

    #Clone
    driver.find_element(By.XPATH, '//*[@id="kt_apps_user_list_datatable"]/table/tbody/tr/td[6]/span/div/button').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[text()="Clone"]').click()
    time.sleep(2)
    driver.find_element(By.XPATH,' //*[@id="title"]').clear()
    time.sleep(1)
    driver.find_element(By.XPATH,' //*[@id="title"]').send_keys("Youtube")
    time.sleep(1)
    driver.find_element(By.XPATH,' //*[@id="link"]').clear()
    time.sleep(1)
    driver.find_element(By.XPATH,' //*[@id="link"]').send_keys("https://www.youtube.com")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="web_link_modal"]/div/div/div[3]/button[1]').click()
    time.sleep(1)

    #webiste again
    driver.get(website)
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="top"]/nav/div[2]/div[2]/div[2]/div[6]/ul/li/a').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="top"]/nav/div[2]/div[2]/div[2]/div[6]/ul/li/ul/div[1]/section/nav/a').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="main"]/div/section/div/div/div/div[1]/div/div/div/a').click()
    time.sleep(4)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)

    #backend
    driver.get(backend)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_aside_menu"]/ul/li[3]/a//*[text()="Pytest Multiple Web Links Automation"]').click()
    time.sleep(1)
    #Data Delete
    driver.find_element(By.XPATH, '//*[@id="kt_apps_user_list_datatable"]/table/thead/tr/th[1]/span/label/span').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_subheader_group_actions_delete_all"]').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'/html/body/div[5]/div/div[3]/button[1]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[5]/div/div[3]/button[1]').click()
    time.sleep(2)
    #Navigation Delete
    driver.find_element(By.XPATH, '//*[@id="kt_header"]/div[2]/div[5]/div[1]/div/div/div[1]/a').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_header"]/div[2]/div[5]/div[2]/div[2]/a[4]/div[2]/div[1]').click()
    time.sleep(1)
    driver.find_element(By.XPATH,' //*[@id="kt_portlet_tools_4"]/div[1]/div[2]/div/a').click()
    time.sleep(1)
    driver.find_element(By.XPATH,' //*[@id="kt_navigation_submit"]').click()
    time.sleep(1)
    print("Tested Completed!")
