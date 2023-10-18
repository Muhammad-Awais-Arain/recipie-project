from test_Menu import *

def test_multiplenews():
    url = os.environ.get("URL")
    if url is None:
        raise ValueError("URL not provided as environment variable")
    driver = initialize_driver(url)
    backend_login(driver)
    try:
        add_menu_item_and_navigate("Pytest Multiple News Automation", "Multiple News", "module", driver)

        num_runs = 1

        # Loop through the code block num_runs times
        for i in range(num_runs):
            driver.find_element(By.XPATH, '//*[@id="kt-content"]/div/div[1]/div[2]/div/div[1]/a/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="kt_wrapper"]/div[4]/div/div[1]/div/form/div[1]/div[1]/div/input[1]').send_keys("News Automation ", +i)
            driver.find_element(By.XPATH, '//*[@id="kt_wrapper"]/div[4]/div/div[1]/div/form/div[1]/div[2]/div/input').send_keys("The Script for Automating News")
            driver.execute_script("CKEDITOR.instances['editor1'].setData(arguments[0]);", LoremIpsum)
            driver.find_element(By.XPATH, '//*[@id="kt_wrapper"]/div[4]/div/div[1]/div/form/div[2]/div/div/div[2]/button').click()
            time.sleep(2)
        driver.quit()


        # #Checking on Web
        # time.sleep(2)
        # driver.get(website)
        # time.sleep(2)
        # driver.find_element(By.XPATH, '//*[@id="top"]/nav/div[2]/div[2]/div[2]/div[6]/ul/li/a').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="top"]/nav/div[2]/div[2]/div[2]/div[6]/ul/li/ul/div[1]/section/nav/a').click()
        # time.sleep(2)
        # driver.find_element(By.XPATH, '//*[@id="hiddenresult"]/div/div[2]/a/h5').click()
        # time.sleep(2)
        #
        #
        # #Backend for privacy change
        # driver.get(backend)
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="kt_aside_menu"]/ul/li[3]/a//*[text()="Pytest Multiple News Automation"]').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="kt_apps_user_list_datatable"]/table/tbody/tr/td[5]/span/div/button').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '/html/body/div[7]/a[1]').click()
        # time.sleep(1)
        #
        #
        # #again website
        # driver.get(website)
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="top"]/nav/div[2]/div[2]/div[2]/div[6]/ul/li/a').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH,'//*[@id="top"]/nav/div[2]/div[2]/div[2]/div[6]/ul/li/ul/div[1]/section/nav/a').click()
        # time.sleep(2)
        # driver.find_element(By.XPATH, '//*[@id="hiddenresult"]/div/div[2]/a/h5').click()
        # time.sleep(2)
        #
        #
        # #Login into website for privacy
        # driver.find_element(By.XPATH, '//*[@id="login-message-popup"]/div/div/div[2]/p/a[1]').click()
        # time.sleep(2)
        # driver.find_element(By.XPATH, '//*[@id="generalSearch"]').send_keys("henry@mailinator.com")
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="login-modal"]/div/div/form/div/div[3]/div[3]/span/div/input').send_keys("henry")
        # time.sleep(1)
        #
        # #Checking After login
        # driver.find_element(By.XPATH, '//*[@id="login-modal"]/div/div/form/div/div[3]/div[5]/button').click()
        # time.sleep(6)
        # driver.find_element(By.XPATH, '//*[@id="top"]/nav/div[2]/div[2]/div[2]/div[6]/ul/li/a').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH,'//*[@id="top"]/nav/div[2]/div[2]/div[2]/div[6]/ul/li/ul/div[1]/section/nav/a').click()
        # time.sleep(2)
        # driver.find_element(By.XPATH, '//*[@id="hiddenresult"]/div/div[2]/a/h5').click()
        # time.sleep(2)
        #
        # # Backend for Unpublish
        # driver.get(backend)
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="kt_aside_menu"]/ul/li[3]/a//*[text()="Pytest Multiple News Automation"]').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="kt_apps_user_list_datatable"]/table/tbody/tr/td[6]/span/div/button/i').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '/html/body/div[7]/a[2]').click()
        # time.sleep(3)
        # # again website for checking unpublish
        # driver.get(website)
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="top"]/nav/div[2]/div[2]/div[2]/div[6]/ul/li/a').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH,  '//*[@id="top"]/nav/div[2]/div[2]/div[2]/div[6]/ul/li/ul/div[1]/section/nav/a').click()
        # time.sleep(2)
        #
        #
        # # Backend for Edit
        # driver.get(backend)
        # driver.find_element(By.XPATH, '//*[@id="kt_aside_menu"]/ul/li[3]/a//*[text()="Pytest Multiple News Automation"]').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="kt_apps_user_list_datatable"]/table/tbody/tr/td[8]/span/div/button').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '/html/body/div[7]/ul/li[1]/a').click()
        # time.sleep(1)
        # driver.execute_script("CKEDITOR.instances['editor1'].setData('After Editing Description')")
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="kt_wrapper"]/div[4]/div/div[1]/div/form/div[1]/div[6]/div/div/div/span[3]').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="kt_wrapper"]/div[4]/div/div[1]/div/form/div[2]/div/div/div[2]/button').click()
        # time.sleep(1)

        # #View Details
        # driver.find_element(By.XPATH, '//*[@id="kt_apps_user_list_datatable"]/table/tbody/tr/td[8]/span/div/button').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '/html/body/div[7]/ul/li[3]/a').click()
        # time.sleep(3)
        # driver.find_element(By.XPATH, '//*[@id="kt_quick_panel_close_btn"]').click()
        # time.sleep(1)
        #
        # #History
        # driver.find_element(By.XPATH, '//*[@id="kt_apps_user_list_datatable"]/table/tbody/tr/td[8]/span/div/button').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '/html/body/div[7]/ul/li[5]/a').click()
        # time.sleep(4)
        # driver.find_element(By.XPATH, '//*[@id="kt-content"]/div/div[1]/div[2]/div/a').click()
        # time.sleep(1)
        #
        # #Clone
        # driver.find_element(By.XPATH, '//*[@id="kt_apps_user_list_datatable"]/table/tbody/tr/td[8]/span/div/button').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '/html/body/div[7]/ul/li[4]/a').click()
        # time.sleep(1)
        # driver.execute_script("CKEDITOR.instances['editor1'].setData('Clone of Multiple News Automation')")
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="kt_wrapper"]/div[4]/div/div[1]/div/form/div[2]/div/div/div[2]/button').click()
        # time.sleep(1)
        #
        # #Select All for Delete
        # driver.find_element(By.XPATH, '//*[@id="kt_apps_user_list_datatable"]/table/thead/tr/th[1]/span/label/span').click()
        # time.sleep(2)
        # driver.find_element(By.XPATH, '//*[@id="kt_subheader_group_actions_delete_all"]').click()
        # time.sleep(2)
        # driver.find_element(By.XPATH, '/html/body/div[7]/div/div[3]/button[1]').click()
        # time.sleep(2)
        # driver.find_element(By.XPATH, '/html/body/div[7]/div/div[3]/button[1]').click()
        # time.sleep(2)
        # driver.find_element(By.XPATH, '//*[@id="kt_header"]/div[2]/div[5]/div[1]/div/div/div[1]/a').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="kt_header"]/div[2]/div[5]/div[2]/div[2]/a[4]/div[2]/div[1]').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[1]/div[2]/div/a').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="kt_navigation_submit"]').click()
        # driver.execute_script('alert("Test Add Multiple News executed Succesfully")')
        # time.sleep(3)
        # driver.quit()
        # print("Automated Sucessfully")
    except Exception as e:
        # If an exception occurs, close the driver and update the status
        status = f"Test stopped due to an error: {str(e)}"
        driver.quit()
    else:
        # If the loop completes successfully, close the driver and update the status
        status = "Test completed successfully"
        driver.quit()
    finally:
        return status
