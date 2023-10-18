from test_Menu import *


def test_Legislative():
    url = os.environ.get("URL")
    if url is None:
        raise ValueError("URL not provided as environment variable")
    
    driver = initialize_driver(url)
    backend_login(driver)
    try:
        add_menu_item_and_navigate("Pytest Legislative Bills Automation", "Legislative Bill", "bill", driver)
        num_runs = 2
        # Loop through the code block num_runs times
        for i in range(num_runs):
        #Add Bill
            driver.find_element(By.XPATH, ' //*[@id="kt-content"]/div/div[1]/div[2]/div/div[1]/a/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[1]/div[1]/div/input').send_keys("Bill ", +i)
            driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[1]/div[2]/div/textarea').send_keys("This bill is for electricity.")
            driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[1]/div[3]/div/textarea').send_keys("This is important to pay electricity bills.")
            driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[1]/div[4]/div/textarea').send_keys("Next Tuesday")
            driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[1]/div[5]/div/input').send_keys("https://www.avialdosolutions.com")
            driver.execute_script("CKEDITOR.instances['editor1'].setData(arguments[0]);", LoremIpsum)
            driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[1]/div[8]/div/tags/span').send_keys("awais@linkedunion.com")
            driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[2]/div/div/div[2]/button').click()
            time.sleep(1)

        #Website
        click_element_by_partial_url("/bills/bill-listing/pytest-legislative-bills-automation/")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 2);")
        time.sleep(2)
        JSscript = "window.location.href = $('#hiddenresult').first('.data-pagination').find('.view-all-btn').attr('href');"
        driver.execute_script(JSscript)

        time.sleep(2)
        driver.execute_script('$(".learn_more").click();')
        time.sleep(2)
        name = """Dear Senators,
        As a concerned community member, I support Bill and urge your committee to pass the bill.

        Mahalo


        Awais

        """
        testimony =  wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'testimony_fetch')))
        testimony.clear()
        time.sleep(1)
        testimony.send_keys(name)
        time.sleep(1)
        submit =  wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'bill_submit')))
        submit.click()
        time.sleep(3)


        # #backend
        # driver.switch_to.window(driver.window_handles[0])

        # #Privacy Change
        # driver.find_element(By.XPATH, '//*[@id="kt_apps_user_list_datatable"]/table/tbody/tr/td[6]/span/div/button/i').click()
        # time.sleep(1)
        # click_private_or_public(True)  # Click on the "Private" option
        # time.sleep(1)

        # #Website
        # driver.get(website)
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="top"]/nav/div[2]/div[2]/div[2]/div[6]/ul/li/a').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="top"]/nav/div[2]/div[2]/div[2]/div[6]/ul/li/ul/div[1]/section/nav/a').click()
        # time.sleep(2)
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 2);")
        # time.sleep(2)
        # driver.execute_script('$(".private_message_popup").click();')
        # #driver.find_element(By.XPATH, '//*[@id="top"]/nav/div[2]/div[2]/div[2]/div[8]/ul/li/a/button').click()
        # time.sleep(3)
        # #Login
        # driver.find_element(By.XPATH, '//*[@id="login-message-popup"]/div/div/div[2]/p/a[1]').click()
        # #time.sleep(2)
        # driver.find_element(By.XPATH, '//*[@id="generalSearch"]').send_keys("henry@mailinator.com")
        # time.sleep(2)
        # driver.find_element(By.XPATH, '//*[@id="login-modal"]/div/div/form/div/div[3]/div[3]/span/div/input').send_keys("henry")
        # time.sleep(2)
        # driver.find_element(By.XPATH, '//*[@id="login-modal"]/div/div/form/div/div[3]/div[5]/button').click()
        # time.sleep(5)
        # driver.find_element(By.XPATH, '//*[@id="top"]/nav/div[2]/div[2]/div[2]/div[6]/ul/li/a').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="top"]/nav/div[2]/div[2]/div[2]/div[6]/ul/li/ul/div[1]/section/nav/a').click()
        # time.sleep(2)
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 2);")
        # time.sleep(2)
        # driver.execute_script(scriptt)
        # time.sleep(3)
        # driver.execute_script('$(".learn_more").click();')
        # time.sleep(2)
        # driver.execute_script('$(".bill_submit").click();')
        # time.sleep(2)
        # driver.find_element(By.XPATH, '//*[@id="top"]/nav/div[2]/div[2]/div[1]/a/img').click()
        # time.sleep(2)
        # #backend
        # driver.get(backend)
        # #Side Menu Click
        # driver.find_element(By.XPATH, '//*[@id="kt_aside_menu"]/ul/li[3]/a//*[text()="Pytest Legislative Bills Automation"]').click()
        # time.sleep(1)
        # #Status Change
        # driver.find_element(By.XPATH, '//*[@id="kt_apps_user_list_datatable"]/table/tbody/tr/td[7]/span/div/button/i').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '/html/body/div[7]/a[2]').click()
        # time.sleep(2)
        # #Website
        # driver.get(website)
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="top"]/nav/div[2]/div[2]/div[2]/div[6]/ul/li/a').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="top"]/nav/div[2]/div[2]/div[2]/div[6]/ul/li/ul/div[1]/section/nav/a').click()
        # time.sleep(2)
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 2);")
        # time.sleep(2)
        # # backend
        # driver.get(backend)
        # # Side Menu Click
        # driver.find_element(By.XPATH, '//*[@id="kt_aside_menu"]/ul/li[3]/a//*[text()="Pytest Legislative Bills Automation"]').click()
        # time.sleep(1)

        # driver.find_element(By.XPATH,'//*[@id="kt_apps_user_list_datatable"]/table/tbody/tr/td[8]/span/div/button/i').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '/html/body/div[7]/ul/li[1]/a/span').click()
        # time.sleep(2)
        # #Edit
        # driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[1]/div[1]/div/input').clear()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[1]/div[1]/div/input').send_keys("Bill 1 After Edit")
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[1]/div[3]/div/textarea').clear()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[1]/div[3]/div/textarea').send_keys("This is a union bill")
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[1]/div[10]/div/div/div/span[3]').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[2]/div/div/div[2]/button').click()
        # time.sleep(2)
        # #View
        # driver.find_element(By.XPATH, '//*[@id="kt_apps_user_list_datatable"]/table/tbody/tr/td[8]/span/div/button').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '/html/body/div[7]/ul/li[3]/a').click()
        # time.sleep(4)
        # driver.find_element(By.XPATH, '//*[@id="kt_quick_panel_close_btn"]').click()
        # time.sleep(2)

        # #History
        # driver.find_element(By.XPATH, '//*[@id="kt_apps_user_list_datatable"]/table/tbody/tr/td[8]/span/div/button').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '/html/body/div[7]/ul/li[5]/a').click()
        # time.sleep(4)
        # driver.find_element(By.XPATH, '//*[@id="kt-content"]/div/div[1]/div[2]/div/a').click()
        # time.sleep(2)

        # #Clone
        # driver.find_element(By.XPATH, '//*[@id="kt_apps_user_list_datatable"]/table/tbody/tr/td[8]/span/div/button').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '/html/body/div[7]/ul/li[4]/a/span').click()
        # time.sleep(2)

        # driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[1]/div[1]/div/input').clear()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[1]/div[1]/div/input').send_keys("Bill 1 clone")

        # driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[1]/div[3]/div/textarea').clear()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[1]/div[3]/div/textarea').send_keys("This is a union bill Clone")
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[2]/div/div/div[2]/button').click()
        # time.sleep(2)

        # # Website
        # driver.get(website)
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="top"]/nav/div[2]/div[2]/div[2]/div[6]/ul/li/a').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="top"]/nav/div[2]/div[2]/div[2]/div[6]/ul/li/ul/div[1]/section/nav/a').click()
        # time.sleep(2)
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 2);")
        # time.sleep(2)
        # driver.execute_script(scriptt)
        # time.sleep(2)
        # driver.execute_script('$(".learn_more").click();')
        # time.sleep(2)
        # driver.execute_script('$(".bill_submit").click();')
        # time.sleep(3)
        # driver.find_element(By.XPATH, '//*[@id="top"]/nav/div[2]/div[2]/div[1]/a/img').click()
        # time.sleep(2)
        # # backend
        # driver.get(backend)
        # # Side Menu Click
        # driver.find_element(By.XPATH, '//*[@id="kt_aside_menu"]/ul/li[3]/a//*[text()="Pytest Legislative Bills Automation"]').click()
        # time.sleep(1)
        # #Delete
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
        # driver.execute_script('$(".kt-margin-l-5").click()')
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="kt_navigation_submit"]').click()
        # time.sleep(1)
        # print("Legislative bill Automation Test Completed!")
        driver.quit()
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