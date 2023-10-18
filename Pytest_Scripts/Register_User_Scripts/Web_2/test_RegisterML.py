from Test_SetUp import *


def test_Register(test_setup, test_UserDetails):

    toggle_settings("off", "off")
    time.sleep(1)
    # copying the temp email and storing it in email variable for CSV
    email = get_temp_email()
    time.sleep(1)
    register_user()
    time.sleep(1)
    driver.find_element(By.NAME, 'first_name').send_keys(test_UserDetails['firstName'])
    driver.find_element(By.NAME, 'last_name').send_keys(test_UserDetails['lastName'])
    driver.find_element(By.NAME, 'email').send_keys(Keys.CONTROL, 'v')
    driver.find_element(By.NAME, 'password').send_keys(test_UserDetails['password'])

    #Submit User data
    SubmitWeb = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "submit_register")))
    SubmitWeb.click()
    time.sleep(3)

    click_magic_link()
    close_notification()


    user_details = test_UserDetails
    save_user_details_to_csv(user_details, email)
