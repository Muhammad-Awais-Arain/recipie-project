from test_SetUp import *


def test_2FARegister(test_setup, test_UserDetails):
    
    toggle_settings("on", "off", "off")

    #Now Register a User in Backend
    add_member(test_UserDetails['firstName'], test_UserDetails['lastName'], test_UserDetails["DOB"], test_UserDetails['employeeID'], test_UserDetails['SSN'])

    #GOTO TEMP-MAIL.ORG TO COPY THE EMAIL ADDRESS
    email = get_temp_email()
    time.sleep(1)
    #GOTO WEBSITE FOR REGISTERING A USER
    register_user()
    time.sleep(1)
    driver.find_element(By.NAME, 'first_name').send_keys(test_UserDetails['firstName'])
    driver.find_element(By.NAME, 'last_name').send_keys(test_UserDetails['lastName'])
    driver.find_element(By.NAME, 'ssn').send_keys(test_UserDetails['SSN'])
    driver.find_element(By.NAME, 'dob').send_keys(test_UserDetails["DOB"])
    driver.find_element(By.NAME, 'register_email').send_keys(Keys.CONTROL, 'v')
    driver.find_element(By.NAME, 'register_password').send_keys(test_UserDetails['password'])

    SubmitWeb = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "Forms_web_btn_primary__IPULW")))
    SubmitWeb.click()
    time.sleep(1)
    
    click_magic_link()
    user_details = test_UserDetails
    save_user_details_to_csv(user_details, email)

    print("User Registered Successfully!")
