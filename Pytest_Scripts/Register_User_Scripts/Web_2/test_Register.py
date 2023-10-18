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

    #Switch to Email Tab to Copy the code
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(4)
    verification_code = get_verification_code()

    time.sleep(1)
    #Switch to Website to paste the code
    driver.switch_to.window(driver.window_handles[2])
    time.sleep(1)

    enter_verification_code(verification_code)

    time.sleep(7)
    close_notification()
    #User registered

    user_details = test_UserDetails
    save_user_details_to_csv(user_details, email)
