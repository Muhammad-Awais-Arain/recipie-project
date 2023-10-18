from Test_SetUp import *

def test_ContinueTwoFacotor(test_setup, test_UserDetails):

    toggle_settings("on", "on", "on")


    # GOTO TEMP-MAIL.ORG TO COPY THE EMAIL ADDRESS
    email = get_temp_email()
    time.sleep(1)

    # GOTO WEBSITE FOR REGISTERING A USER
    register_user()


    time.sleep(1)
    driver.find_element(By.NAME, 'first_name').send_keys(test_UserDetails['firstName'])
    driver.find_element(By.NAME, 'last_name').send_keys(test_UserDetails['lastName'])
    driver.find_element(By.NAME, 'employee_id').send_keys(test_UserDetails['employeeID'])
    driver.find_element(By.NAME, 'date_of_birth').send_keys(test_UserDetails["DOB"])
    driver.find_element(By.NAME, 'email').send_keys(Keys.CONTROL, 'v')
    driver.find_element(By.NAME, 'password').send_keys(test_UserDetails['password'])
    time.sleep(1)

    # Submit User data
    SubmitWeb = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "submit_register")))
    SubmitWeb.click()
    time.sleep(3)
    #Continue Button
    SubmitWeb = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "continue_save")))
    SubmitWeb.click()

    # Switch to Email Tab to Copy the code
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(4)

    verification_code = get_verification_code()

    time.sleep(1)
    #Switch to Website to paste the code
    driver.switch_to.window(driver.window_handles[2])
    enter_verification_code(verification_code)
    time.sleep(1)



    #CODE HERE FOR APPROVING MEMBER
    # GO BACK TO BACKEND TO ACCEPT MEMBER
    click_member_approval_with_firstname(test_UserDetails['firstName'])

    # To website to check login
    login_with_email_and_password(email, test_UserDetails['password'])

    user_details = test_UserDetails
    save_user_details_to_csv(user_details, email)

    print("Member Approval Finished!")
