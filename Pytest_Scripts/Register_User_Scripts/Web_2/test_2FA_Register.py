
from Test_SetUp import *


def test_Register(test_setup, test_UserDetails):

    toggle_settings("on", "off", "off")

    #Now Register a User in Backend
    add_member(test_UserDetails['firstName'], test_UserDetails['lastName'], test_UserDetails["DOB"], test_UserDetails['employeeID'], test_UserDetails['SSN'])

    #GOTO TEMP-MAIL.ORG TO COPY THE EMAIL ADDRESS
    email = get_temp_email()


    #GOTO WEBSITE FOR REGISTERING A USER
    register_user()
    driver.find_element(By.NAME, 'first_name').send_keys(test_UserDetails['firstName'])
    driver.find_element(By.NAME, 'last_name').send_keys(test_UserDetails['lastName'])
    driver.find_element(By.NAME, 'employee_id').send_keys(test_UserDetails['employeeID'])
    driver.find_element(By.NAME, 'date_of_birth').send_keys(test_UserDetails["DOB"])
    driver.find_element(By.NAME, 'email').send_keys(Keys.CONTROL, 'v')
    driver.find_element(By.NAME, 'password').send_keys(test_UserDetails['password'])
    time.sleep(1)

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
    enter_verification_code(verification_code)
    time.sleep(7)

    close_notification()

    user_details = test_UserDetails
    save_user_details_to_csv(user_details, email)
    