from test_Menu import *
def test_UnionRepresentative(test_setup):
    user_menu_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/navigation/"]')))
    user_menu_element.click()

    #MENU ADD
    driver.find_element(By.XPATH, '//*[@id="kt_navigation_form"]/div/div/div[1]/div[2]/div/div/a/span').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_navigation_submit"]').click()
    time.sleep(5)


    #CHANGING MENU NAME
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
        titlee = elements[-1]
        titlee.clear()
        titlee.send_keys("Pytest Union Representative Automation")

    elements = driver.find_elements(By.CSS_SELECTOR, "select[name$='[action]']")

    # get the length of the list
    n = len(elements)

    # find the last element and click on it
    if n > 0:
        action_selectpicker = elements[-1]
        select = Select(action_selectpicker)
        select.select_by_visible_text("Union Representative")
    else:
        # handle the case where there are no elements
        print("No elements found")

    time.sleep(1)

    save_button = wait.until(EC.presence_of_element_located((By.ID, "kt_navigation_submit")))
    # move to the element
    actions.move_to_element(save_button).perform()
    # click the element
    save_button.click()

    time.sleep(5)
    # SIDE MENU EVENT CLICK
    side_element = driver.find_element(By.XPATH, "//a[starts-with(@href, '/union-representative/pytest-union-representative-automation/')]")
    driver.execute_script("arguments[0].scrollIntoView();", side_element)
    # Click the element
    side_element.click()

    time.sleep(2)
    num_runs = 3
    # Loop through the code block num_runs times
    for i in range(num_runs):
    #Add Representative
        driver.find_element(By.XPATH, '//*[@id="kt-content"]/div/div[1]/div[2]/div/div[1]/a/button').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[1]/div[1]/div/input').send_keys("Union Representative Automation ", +i)
        driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[1]/div[2]/div/input').send_keys("Linked Union")
        driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[1]/div[3]/div/input').send_keys('+923347386649')
        driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[1]/div[6]/div/input').send_keys("aawiii63@gmail.com")
        driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[1]/div[7]/div/input').send_keys("1610 Kathy St, EMMETT, IDAHO, 83617")
        driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[1]/div[8]/div/input').send_keys("www.google.com")
        driver.execute_script("CKEDITOR.instances['editor1'].setData(arguments[0]);", LoremIpsum)
        time.sleep(1)
        # img_upload_elem = driver.find_element(By.ID, 'kt_dropzone_1')
        # img_upload_elem.click()
        # img_upload_elem.send_keys('../images/software_testing.jpg')
        # time.sleep(1)
        driver.find_element(By.XPATH, ' //*[@id="kt_content"]/div[2]/div/form/div[2]/div/div/div[2]/button').click()
        time.sleep(1)

    #Website
    driver.get(website)
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="top"]/nav/div[2]/div[2]/div[2]/div[6]/ul/li/a').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="top"]/nav/div[2]/div[2]/div[2]/div[6]/ul/li/ul/div[1]/section/nav/a').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="hiddenresult"]/div/div/div[1]/div[3]/h5').click()
    time.sleep(4)
    driver.find_element(By.XPATH,'//*[@id="union-detail-modal"]/div/div/div[2]/button').click()
    time.sleep(2)

    #Backend for Edit
    driver.get(backend)
    driver.find_element(By.XPATH, '//*[@id="kt_aside_menu"]/ul/li[3]/a//*[text()="Pytest Union Representative Automation"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_apps_user_list_datatable"]/table/tbody/tr/td[14]/span/div/button').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[7]/ul/li[1]/a').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[1]/div[1]/div/input').clear()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[1]/div[1]/div/input').send_keys("Union Representative Automation After Edit")
    time.sleep(1)
    driver.find_element(By.XPATH,' //*[@id="kt_content"]/div[2]/div/form/div[1]/div[8]/div/input').send_keys("www.facebook.com")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[1]/div[13]/div/div/div/span[3]').click()
    time.sleep(1)
    driver.find_element(By.XPATH,' //*[@id="kt_content"]/div[2]/div/form/div[2]/div/div/div[2]/button').click()
    time.sleep(2)

    #Clone
    driver.find_element(By.XPATH, '//*[@id="kt_aside_menu"]/ul/li[3]/a//*[text()="Pytest Union Representative Automation"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_apps_user_list_datatable"]/table/tbody/tr/td[14]/span/div/button').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[7]/ul/li[4]/a').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[1]/div[1]/div/input').clear()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[1]/div[1]/div/input').send_keys("Union Representative Automation After Clone")
    time.sleep(1)
    driver.find_element(By.XPATH, ' //*[@id="kt_content"]/div[2]/div/form/div[1]/div[8]/div/input').send_keys("www.linkedin.com")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[1]/div[13]/div/div/div/span[3]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, ' //*[@id="kt_content"]/div[2]/div/form/div[2]/div/div/div[2]/button').click()
    time.sleep(2)

    #View
    driver.find_element(By.XPATH, '//*[@id="kt_aside_menu"]/ul/li[3]/a//*[text()="Pytest Union Representative Automation"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_apps_user_list_datatable"]/table/tbody/tr/td[14]/span/div/button').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[7]/ul/li[3]/a').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="kt_quick_panel_close_btn"]').click()
    time.sleep(1)

    #Website for checking
    driver.get(website)
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="top"]/nav/div[2]/div[2]/div[2]/div[6]/ul/li/a').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="top"]/nav/div[2]/div[2]/div[2]/div[6]/ul/li/ul/div[1]/section/nav/a').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="hiddenresult"]/div/div/div[1]/div[3]/h5').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="login-message-popup"]/div/div/div[2]/p/a[1]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="generalSearch"]').send_keys("henry@mailinator.com")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="login-modal"]/div/div/form/div/div[3]/div[3]/span/div/input').send_keys("henry")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="login-modal"]/div/div/form/div/div[3]/div[5]/button').click()
    time.sleep(4)
    driver.find_element(By.XPATH, '//*[@id="top"]/nav/div[2]/div[2]/div[2]/div[6]/ul/li/a').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="top"]/nav/div[2]/div[2]/div[2]/div[6]/ul/li/ul/div[1]/section/nav/a').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="hiddenresult"]/div/div/div[1]/div[3]/h5').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="union-detail-modal"]/div/div/div[2]/button').click()
    time.sleep(1)
    #Backend Delete
    driver.get(backend)
    driver.find_element(By.XPATH, '//*[@id="kt_aside_menu"]/ul/li[3]/a//*[text()="Pytest Union Representative Automation"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_apps_user_list_datatable"]/table/thead/tr/th[2]/span/label/span').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="kt_subheader_group_actions_delete_all"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[7]/div/div[3]/button[1]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[7]/div/div[3]/button[1]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_header"]/div[2]/div[5]/div[1]/div/div/div[1]/a').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_header"]/div[2]/div[5]/div[2]/div[2]/a[4]/div[2]/div[1]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[1]/div[2]/div/a').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kt_navigation_submit"]').click()
    time.sleep(1)
    driver.quit()
    print("Tested Completed!")
