from test_Menu import *


def test_OMW(test_setup):

    add_menu_item_and_navigate("Organize My Workplace Automation", "Organize My Workplace", "orgainze-my-workplace")

    click_element_by_partial_url("/organize-my-workplace/organize-my-workplace-automation")

    #Filling Form
    driver.find_element(By.XPATH,' //*[@id="main"]/section[2]/div/div/div/form/div/div[1]/div[1]/div/span/input').send_keys("Henry")
    driver.find_element(By.XPATH, '//*[@id="main"]/section[2]/div/div/div/form/div/div[1]/div[2]/div/span/input').send_keys("Mailinator")
    driver.find_element(By.XPATH, '//*[@id="main"]/section[2]/div/div/div/form/div/div[2]/div[1]/div/span/input').send_keys("henry@mailinator.com")
    driver.find_element(By.XPATH, '//*[@id="main"]/section[2]/div/div/div/form/div/div[2]/div[2]/div/span/input').send_keys("+1234123412")
    driver.find_element(By.XPATH, '//*[@id="main"]/section[2]/div/div/div/form/div/div[3]/div/div/span/textarea').send_keys("1610 Kathy St, EMMETT, IDAHO, 83617")
    time.sleep(1)

    # Select state
    select_dropdown_option("state_select", "NY")
    time.sleep(1)

    # Select city
    select_dropdown_option("city_dropdown", "HOWARD BEACH")
    time.sleep(1)

    #Description and button click
    driver.find_element(By.XPATH, '//*[@id="main"]/section[2]/div/div/div/form/div/div[5]/div[1]/div/span/input').send_keys("75100")
    driver.find_element(By.XPATH, '//*[@id="main"]/section[2]/div/div/div/form/div/div[5]/div[2]/div/span/input').send_keys("Test")
    driver.find_element(By.XPATH, '//*[@id="main"]/section[2]/div/div/div/form/div/div[6]/div[1]/div/span/input').send_keys("SQA")
    driver.find_element(By.XPATH, '//*[@id="main"]/section[2]/div/div/div/form/div/div[6]/div[2]/div/span/input').send_keys("100")
    driver.find_element(By.XPATH, '//*[@id="main"]/section[2]/div/div/div/form/div/div[7]/div/div/span/textarea').send_keys("Description here!")
    time.sleep(1)
    driver.execute_script('$(".text-center").find("button").click();')
    time.sleep(3)

    
    handles = driver.window_handles
    # Switch to the new tab
    driver.switch_to.window(handles[0])
    driver.refresh()
    time.sleep(3)
    #Delete DATA
