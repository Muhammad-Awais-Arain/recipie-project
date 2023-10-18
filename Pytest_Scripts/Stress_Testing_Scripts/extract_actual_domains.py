from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import csv
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


# Set up Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
chrome_options.add_argument("--window-size=1920x1080")  # Set window size

# Initialize the WebDriver with the specified options
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.maximize_window()
wait = WebDriverWait(driver, 10)
actions = ActionChains(driver)


def extract_live_domains(email, password):
    driver.get('https://desibook.admin.linkedunion.com/') 
    driver.find_element(By.NAME, 'email').send_keys(email)
    driver.find_element(By.NAME, 'password').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="kt_login_signin_submit"]').click()
    time.sleep(2)

    code = "345876"
    input_fields = driver.find_elements(By.CSS_SELECTOR, 'input[name="letters[]"]')

    for index, field in enumerate(input_fields):
        if index < len(code):
            field.send_keys(code[index])

    driver.find_element(By.ID, 'kt_verify_two_factor_code').click()
    print("Login Successful")
    time.sleep(3)
    dropdown_element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "kt-user-card-v2__name")))
    dropdown_element.click()

    time.sleep(1)
    user_menu_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/union-onboarding/"]')))
    user_menu_element.click()

    time.sleep(2)
    # Find the button element that triggers the App dropdown
    dropdown_button = driver.find_element(By.XPATH, '//*[@id="kt_subheader"]/div/div[2]/div[1]/div[2]/div/button')
    # Click on the dropdown to open it
    dropdown_button.click()

    # Now you can interact with the dropdown items or click on the desired item if it's visible
    # For example, clicking on the "Website" option:
    website_option = driver.find_element(By.XPATH, '//div[contains(@class, "onboarding_tables") and contains(@class, "website_datatable")]//a')
    website_option.click()

    time.sleep(2)
    # Find the button element that triggers the dropdown
    filter_button = driver.find_element(By.XPATH, '//*[@id="kt_subheader"]/div/div[2]/div[2]/div/button')
    # Click on the dropdown to open it
    filter_button.click()

    #Pending Hide
    pen_checkbox = driver.find_element(By.XPATH, '//*[@id="kt_subheader"]/div/div[2]/div[2]/div/div/div[3]/div/div[1]/li/a/label')
    # Click on the element
    pen_checkbox.click()
    #In Progress 
    InPro_checkbox = driver.find_element(By.XPATH, '//*[@id="kt_subheader"]/div/div[2]/div[2]/div/div/div[3]/div/div[5]/li/a/label')
    # Click on the element
    InPro_checkbox.click()
    #Needs Dev
    NeedsDev_checkbox = driver.find_element(By.XPATH, '//*[@id="kt_subheader"]/div/div[2]/div[2]/div/div/div[3]/div/div[6]/li/a/label')
    # Click on the element
    NeedsDev_checkbox.click()

    #IN REVIEW
    InRev_checkbox = driver.find_element(By.XPATH, '//*[@id="kt_subheader"]/div/div[2]/div[2]/div/div/div[3]/div/div[8]/li/a/label')
    # Click on the element
    InRev_checkbox.click()
    #REJECTED
    ReJEC_checkbox = driver.find_element(By.XPATH, '//*[@id="kt_subheader"]/div/div[2]/div[2]/div/div/div[3]/div/div[10]/li/a/label')
    # Click on the element
    ReJEC_checkbox.click()

    # Wait for the dropdown to open (if necessary)
    # Add a wait if the dropdown is loaded dynamically and takes time to appear
    time.sleep(1)

    # Find the element with the "Live" text
    live_checkbox = driver.find_element(By.XPATH, '//*[@id="kt_subheader"]/div/div[2]/div[2]/div/div/div[3]/div/div[3]/li/a/label')

    # Click on the element
    live_checkbox.click()
    # Wait for the page to load or for the desired actions to complete
    time.sleep(3)
    
    # Find the dropdown button that triggers the page dropdown options
    dropdown_button = driver.find_element(By.XPATH, '//*[@id="kt_union_onboarding_list_datatable"]/div/div/div/button')
    # Click on the dropdown button to open it
    dropdown_button.click()
    time.sleep(1)

    # Find the option with the value "100" and click it
    option_100 = driver.find_element(By.XPATH, '//option[@value="100"]')
    option_100.click()
    time.sleep(10)

    start_page = 1
    max_pages = 3

    href_list = scrape_multiple_pages(start_page, max_pages)
    return href_list

  
def scrape_multiple_pages(start_page, max_pages):
    href_list = []

    for page_number in range(start_page, start_page + max_pages):
        try:
            # Construct the XPATH based on the page number
            page_xpath = f'//*[@id="kt_union_onboarding_list_datatable"]/div/ul/li/a[@title="{page_number}"]'

            # Wait for the page element and click on it
            page_element = wait.until(EC.element_to_be_clickable((By.XPATH, page_xpath)))
            driver.execute_script("arguments[0].scrollIntoView(true);", page_element)
            page_element.click()

            # Wait for the page to load
            time.sleep(10)

            # Extract domain URLs from the current page
            href_list += extract_domain_urls_from_page()

        except Exception as e:
            print("Error:", e)
        
    return href_list



def extract_domain_urls_from_page():
    href_list = []
    try:
        elements = driver.find_elements(By.CSS_SELECTOR, 'td[data-field="domain_url"] a')
        for element in elements:
            url = element.get_attribute("href")
            href_list.append(url)
    except Exception as e:
        print("Error:", e)
    return href_list


def main():
    email = 'luautomatedguru@linkedunion.com'
    password = 'Automation@1234'

    response = extract_live_domains(email, password)

    # Write the results to a Python file
    with open('website_domains_production.py', 'w') as pyfile:
        pyfile.write('DOMAINS = [\n')
        for href in response:
            pyfile.write(f'    "{href}",\n')
        pyfile.write(']\n')


if __name__ == "__main__":
    main()
