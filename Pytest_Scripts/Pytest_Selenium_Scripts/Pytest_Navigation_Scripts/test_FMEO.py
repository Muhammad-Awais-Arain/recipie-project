from test_Menu import *

def test_FEMO(test_setup):
    
    add_menu_item_and_navigate("Pytest FMEO Automation", "Find My Elected Officials", "find-my-elected-officials")
    #WEBSITE
    click_element_by_partial_url("/find-my-elected/pytest-fmeo-automation")
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="inputaddress"]').send_keys("1610 Kathy St, EMMETT, IDAHO, 83617")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="main"]/section[2]/div/div/div/div[1]/div/form/span/div/button').click()
    time.sleep(1)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)

    #Delete
    # Retrieve the window handles
    handles = driver.window_handles

    # Switch to the first window
    driver.switch_to.window(handles[0])
    time.sleep(1)
    DropDown = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "kt-user-card-v2__name")))
    DropDown.click()
    user_menu_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/navigation/"]')))
    user_menu_element.click()
    driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[1]/div[2]/div/a/i').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_navigation_submit"]').click()
    time.sleep(3)
    driver.quit()
    print("Test Completed!")
