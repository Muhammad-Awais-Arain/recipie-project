from Test_SetUp import *

def test_FailTwoFacotor(test_setup, test_UserDetails):

    toggle_settings("on", "off", "off")

    # GOTO WEBSITE FOR REGISTERING A USER
    register_user()

    driver.find_element(By.NAME, 'first_name').send_keys(test_UserDetails['firstName'])
    driver.find_element(By.NAME, 'last_name').send_keys(test_UserDetails['lastName'])
    driver.find_element(By.NAME, 'employee_id').send_keys(test_UserDetails['employeeID'])
    driver.find_element(By.NAME, 'date_of_birth').send_keys(test_UserDetails["DOB"])
    driver.find_element(By.NAME, 'email').send_keys("awais@linkedunion.com")
    driver.find_element(By.NAME, 'password').send_keys(test_UserDetails['password'])
    time.sleep(1)

    # Submit User data
    SubmitWeb = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "submit_register")))
    SubmitWeb.click()

    driver.execute_script('alert("Successfully Executed")')

