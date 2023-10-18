from test_Menu import *


def test_addevent():
    url = os.environ.get("URL")
    if url is None:
        raise ValueError("URL not provided as environment variable")
    
    driver = initialize_driver(url)
    backend_login(driver)
    try:
        add_menu_item_and_navigate("Event Automation", "Event", "event", driver)

        num_runs = 1
        # Loop through the code block num_runs times
        for i in range(num_runs):
            driver.find_element(By.XPATH, '//*[@id="kt-content"]/div/div[1]/div[2]/div/div[1]/a/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[1]/div[1]/div/input').send_keys("Event Automation Using Selenium ", +i)
            #START DATE
            driver.find_element(By.ID, 'kt_datetimepicker_3').click()
            driver.find_element(By.XPATH, '/html/body/div[9]/div[3]/table/tbody/tr[5]/td[2]').click()
            driver.find_element(By.XPATH, '/html/body/div[9]/div[2]/table/tbody/tr/td/fieldset[2]/span[1]').click()
            driver.find_element(By.XPATH, '/html/body/div[9]/div[1]/table/tbody/tr/td/fieldset/span[6]').click()

            #END DATE
            driver.find_element(By.ID, 'kt_datetimepicker_4').click()
            driver.find_element(By.XPATH, '/html/body/div[10]/div[3]/table/tbody/tr[5]/td[3]').click()
            driver.find_element(By.XPATH, '/html/body/div[10]/div[2]/table/tbody/tr/td/fieldset[2]/span[11]').click()
            driver.find_element(By.XPATH, '/html/body/div[10]/div[1]/table/tbody/tr/td/fieldset/span[12]').click()

            #LOCATION
            driver.find_element(By.XPATH, '//*[@id="address"]').send_keys('Karachi, Pakistan')
            driver.find_element(By.NAME, 'details').send_keys('Testing Automation')
            time.sleep(1)
            #Event Added Sucesfully
            driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[2]/div/div/div[2]/button').click()
            time.sleep(1)
            driver.quit()


        #Redirecting to Website for checking
        # click_element_by_partial_url("/events/event-automation/", driver)

        # time.sleep(2)
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(2)
        # driver.execute_script('$(".fc-sticky").click();')
        # time.sleep(3)
        # driver.find_element(By.CLASS_NAME, 'btn-close').click()
        # time.sleep(1)


        # #Coming back to backend for updating the event
        # driver.switch_to.window(driver.window_handles[0])
        # time.sleep(1)
        # #Privacy from public to private
        # driver.find_element(By.XPATH, '//*[@id="kt_apps_user_list_datatable"]/table/tbody/tr/td[9]/span/div/button/i').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '/html/body/div[7]/a[1]').click()
        # time.sleep(1)
        # #checking on website again
        # driver.get(website)
        # time.sleep(1)
        # driver.find_element(By.ID, 'toggleDropdown').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '(//*[text()="Event Automation"])[2]').click()
        # time.sleep(2)
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 2 );")
        # time.sleep(2)
        # driver.execute_script('$(".fc-sticky").click()')
        # time.sleep(2)
        # #Logging In
        # driver.find_element(By.XPATH, '//*[@id="login-message-popup"]/div/div/div[2]/p/a[1]').click()
        # time.sleep(2)
        # driver.find_element(By.XPATH, '//*[@id="generalSearch"]').send_keys("henry@mailinator.com")
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="login-modal"]/div/div/form/div/div[3]/div[3]/span/div/input').send_keys("henry")
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="login-modal"]/div/div/form/div/div[3]/div[5]/button').click()
        # time.sleep(5)
        # #Login Sucesfull
        # driver.find_element(By.ID, 'toggleDropdown').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '(//*[text()="Event Automation"])[2]').click()
        # time.sleep(2)
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 2);")
        # time.sleep(2)
        # driver.execute_script('$(".fc-sticky").click();')
        # time.sleep(3)
        # driver.find_element(By.CLASS_NAME, 'btn-close').click()
        # time.sleep(1)
        # #Coming back to Backend again for updating
        # driver.get(backend)
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="kt_aside_menu"]/ul/li[3]/a//*[text()="Event Automation"]').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="kt_apps_user_list_datatable"]/table/tbody/tr/td[15]/span/div/button').click()
        # time.sleep(1)
        # # EDIT/UPDATE
        # driver.find_element(By.XPATH, '//*[text()="Edit"]').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[1]/div[1]/div/input').send_keys(" ")
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[1]/div[1]/div/input').send_keys("Edited")
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[2]/div/div/div[2]/button').click()
        # time.sleep(1)
        # #CLONE
        # driver.find_element(By.XPATH, '//*[@id="kt_apps_user_list_datatable"]/table/tbody/tr/td[15]/span/div/button').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[text()="Clone"]').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[2]/div/div/div[2]/button').click()
        # time.sleep(1)
        # #Checking on website
        # driver.get(website)
        # driver.find_element(By.ID, 'toggleDropdown').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '(//*[text()="Event Automation"])[2]').click()
        # time.sleep(2)
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(2)
        # driver.execute_script('$(".fc-sticky").click();')
        # time.sleep(3)


        # #Back to backend for History
        # driver.get(backend)
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="kt_aside_menu"]/ul/li[3]/a//*[text()="Event Automation"]').click()
        # time.sleep(1)
        # #Event Delete
        # driver.find_element(By.XPATH, '//*[@id="kt_apps_user_list_datatable"]/table/thead/tr/th[2]/span/label/span').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="kt_subheader_group_actions_delete_all"]').click()
        # time.sleep(2)
        # driver.find_element(By.XPATH, '/html/body/div[7]/div/div[3]/button[1]').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '/html/body/div[7]/div/div[3]/button[1]').click()
        # time.sleep(1)
        # #Navigation Delete
        # time.sleep(2)
        # driver.find_element(By.XPATH, '//*[@id="kt_header"]/div[2]/div[5]/div[1]/div/div/div[1]/a').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="kt_header"]/div[2]/div[5]/div[2]/div[2]/a[4]/div[2]/div[1]').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[1]/div[2]/div/a').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="kt_navigation_submit"]').click()
        # time.sleep(1)
        # driver.execute_script('alert("Test Add Event executed Succesfully")')
        # time.sleep(3)

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

