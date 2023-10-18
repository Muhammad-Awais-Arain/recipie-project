from Test_SetUp import *


def test_Register(test_setup, test_UserDetails):
    #Project Settings
    toggle_settings("off", "on")

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

    ###Get verfication code from the email
    verification_code = get_verification_code()
    #Paste that copied verification code to the website 
    enter_verification_code(verification_code)

    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="login-modal"]/div/div/div[3]/form/div[2]/div[2]/div[2]/button').click()

    time.sleep(1)
    #GO BACK TO BACKEND TO ACCEPT MEMBER
    click_member_approval_with_firstname(test_UserDetails['firstName'])


    # #To website to check login
    login_with_email_and_password(email, test_UserDetails['password'])


    print("Member Approval Finished!")

    user_details = test_UserDetails
    save_user_details_to_csv(user_details, email)

    driver.execute_script('alert("Successfully Executed")')
