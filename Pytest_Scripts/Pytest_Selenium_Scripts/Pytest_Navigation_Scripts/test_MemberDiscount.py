from test_Menu import *


def test_MemberDiscount():
    url = "https://desibook.admin.linkedunion.org"
    # url = os.environ.get("URL")
    if url is None:
        raise ValueError("URL not provided as environment variable")
    driver = initialize_driver(url)
    backend_login(driver)
    try:
        add_menu_item_and_navigate("Member Discount Automation", "Member Discount", "member-discount", driver)

        time.sleep(2)
        num_runs = 1

        # Loop through the code block num_runs times
        for i in range(num_runs):

            driver.find_element(By.XPATH, '//*[@id="kt-content"]/div/div[2]/div/div/div/div[1]/div[2]/div/a').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[1]/div[1]/div/input').send_keys("Member Discount")
            driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[1]/div[2]/div/span/span[1]/span/ul/li/input').send_keys("10%")
            driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[1]/div[3]/div/input').send_keys("www.google.com")
            driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[1]/div[4]/div/textarea').send_keys("Member discount is 10% off")
            driver.execute_script("CKEDITOR.instances['editor1'].setData(arguments[0]);", LoremIpsum)
            driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[2]/div/div/div[2]/button').click()
            time.sleep(1)
        #
        # #website check
        # driver.get(website)
        # time.sleep(2)
        # driver.find_element(By.XPATH, '//*[@id="top"]/nav/div[2]/div[2]/div[2]/div[6]/ul/li/a').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="top"]/nav/div[2]/div[2]/div[2]/div[6]/ul/li/ul/div[1]/section/nav/a').click()
        # time.sleep(2)
        # driver.find_element(By.XPATH, '//*[@id="hiddenresult"]/div/div/div/div[2]/a').click()
        # time.sleep(3)
        #
        # #Backend for privacy
        # driver.get(backend)
        # time.sleep(1)
        # #SIDE MENU EVENT CLICK
        # driver.find_element(By.XPATH, '//*[@id="kt_aside_menu"]/ul/li[3]/a//*[text()="Pytest Member Discount Automation"]').click()
        # time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="kt_apps_user_list_datatable"]/table/tbody/tr/td[7]/span/div/button').click()
        time.sleep(1)
        private_option = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[6]/a[1]")))
        private_option.click()
        #
        # # website check
        # driver.get(website)
        # time.sleep(2)
        # driver.find_element(By.XPATH, '//*[@id="top"]/nav/div[2]/div[2]/div[2]/div[6]/ul/li/a').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="top"]/nav/div[2]/div[2]/div[2]/div[6]/ul/li/ul/div[1]/section/nav/a').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="hiddenresult"]/div/div/div/div[2]/a').click()
        # time.sleep(2)
        # driver.find_element(By.XPATH, '//*[@id="login-message-popup"]/div/div/div[2]/p/a[1]').click()
        # time.sleep(2)
        # #Login
        # driver.find_element(By.XPATH, '//*[@id="generalSearch"]').send_keys("henry@mailinator.com")
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="login-modal"]/div/div/form/div/div[3]/div[3]/span/div/input').send_keys("henry")
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="login-modal"]/div/div/form/div/div[3]/div[5]/button').click()
        # time.sleep(4)
        # driver.find_element(By.XPATH, '//*[@id="top"]/nav/div[2]/div[2]/div[2]/div[6]/ul/li/a').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="top"]/nav/div[2]/div[2]/div[2]/div[6]/ul/li/ul/div[1]/section/nav/a').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="hiddenresult"]/div/div/div/div[2]/a').click()
        # time.sleep(2)
        #
        #
        # # Backend for Edit
        # driver.get(backend)
        # driver.find_element(By.XPATH, '//*[@id="kt_aside_menu"]/ul/li[3]/a//*[text()="Pytest Member Discount Automation"]').click()
        # time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="kt_apps_user_list_datatable"]/table/tbody/tr/td[9]/span/div/button').click()
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, "Edit").click()
        time.sleep(1)
        # assuming driver is your Selenium webdriver object
        # li_elements = driver.find_elements(By.XPATH, '//ul[@class="kt-nav"]/li[position() mod 2 = 1]')
        # for li in li_elements:
        #     edit_link = li.find_element('.//a[contains(@class,"kt-nav__link") and contains(@href,"/edit/")]')
        #     edit_link.click()
            # do your edit operation here

        driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[1]/div[1]/div/input').clear()
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[1]/div[1]/div/input').send_keys("Memeber Discount Edit")
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[2]/div/div/div[2]/button').click()
        time.sleep(1)
        #View
        driver.find_element(By.XPATH, '//*[@id="kt_apps_user_list_datatable"]/table/tbody/tr/td[9]/span/div/button').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[5]/ul/li[3]/a/span').click()
        time.sleep(4)
        driver.find_element(By.XPATH, '//*[@id="kt_quick_panel_close_btn"]/i').click()
        time.sleep(1)
        #History
        driver.find_element(By.XPATH, '//*[@id="kt_apps_user_list_datatable"]/table/tbody/tr/td[9]/span/div/button').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[5]/ul/li[5]/a/span').click()
        time.sleep(4)
        driver.find_element(By.XPATH,' //*[@id="kt-content"]/div/div[1]/div[2]/div/a/i').click()
        time.sleep(1)
        #Clone
        driver.find_element(By.XPATH, '//*[@id="kt_apps_user_list_datatable"]/table/tbody/tr/td[9]/span/div/button').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[5]/ul/li[4]/a/span').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[1]/div[1]/div/input').clear()
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[1]/div[1]/div/input').send_keys("Clone of Member Discount")
        time.sleep(1)
        driver.find_element(By.XPATH,' //*[@id="kt_content"]/div[2]/div/form/div[1]/div[3]/div/input').clear()
        time.sleep(2)
        driver.find_element(By.XPATH,' //*[@id="kt_content"]/div[2]/div/form/div[1]/div[3]/div/input').send_keys('www.linkedunion.com')
        time.sleep(1)
        driver.execute_script("CKEDITOR.instances['editor1'].setData('Clone of Member Discount')")
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[1]/div[8]/div/div/div/span[1]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="kt_content"]/div[2]/div/form/div[2]/div/div/div[2]/button').click()
        time.sleep(1)
        #
        # #Pin Post
        # driver.find_element(By.XPATH, '//*[@id="kt_apps_user_list_datatable"]/table/tbody/tr/td[9]/span/div/button').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '/html/body/div[5]/ul/li[6]/a/span').click()
        # time.sleep(2)
        #
        # #website check last time
        # driver.get(website)
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="top"]/nav/div[2]/div[2]/div[2]/div[6]/ul/li/a').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="top"]/nav/div[2]/div[2]/div[2]/div[6]/ul/li/ul/div[1]/section/nav/a').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="hiddenresult"]/div/div/div/div[2]/a').click()
        # time.sleep(2)
        # time.sleep(3)
        #
        # # Backend for Delete
        # driver.get(backend)
        # driver.find_element(By.XPATH, '//*[@id="kt_aside_menu"]/ul/li[3]/a//*[text()="Pytest Member Discount Automation"]').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="kt_apps_user_list_datatable"]/table/thead/tr/th[1]/span/label/span').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="kt_subheader_group_actions_delete_all"]').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '/html/body/div[5]/div/div[3]/button[1]').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '/html/body/div[5]/div/div[3]/button[1]').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="kt_header"]/div[2]/div[5]/div[1]/div/div/div[1]/a').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="kt_header"]/div[2]/div[5]/div[2]/div[2]/a[4]/div[2]/div[1]').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="kt_portlet_tools_4"]/div[1]/div[2]/div/a').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH, '//*[@id="kt_navigation_submit"]/i').click()
        # time.sleep(4)
        return ("Test Complete!")

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