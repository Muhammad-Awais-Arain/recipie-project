from test_login import *


def test_loginTwo():
    driver.get(backend)
    email = "awais@linkedunion.com"
    password = "Awais@1234"
    wrong_password = "122"

    # Try logging in with wrong credentials multiple times
    for i in range(5):
        login(email, wrong_password)
        for j in range(i):
            driver.find_element(By.ID, 'kt_login_signin_submit').click()
            time.sleep(1)
        login(email, password)
        logout()

    # Unblock the user and log in with correct credentials
    login(email, password)
    unblock_user("Awais")
    logout()

    # Log in again to verify successful login
    login(email, password)
    print("Login Successful")
    logout()


