from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Setup Chrome WebDriver
driver = webdriver.Chrome()

# Open the demo store website
driver.get("http://demostore.supersqa.com")

# Click on "My Account" (consider using more robust locators)
my_account_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "My Account"))
)
my_account_link.click()

# Navigate to the registration page (modify if necessary)
registration_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "My Account"))
)
registration_link.click()

# Enter email address
email_field = driver.find_element(By.XPATH, "//input[@id='reg_email']")
email_field.send_keys("your_email@example.com")

# Leave password field empty

# Click the register button
register_button = driver.find_element(By.XPATH, "//button[normalize-space()='Register']")
register_button.click()

# Verify error message presence (customize based on actual error element)
try:
    error_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//ul[@role='alert']"))
    )
    print("Error message found!")
except TimeoutException:
    print("Error message not found within 10 seconds.")
    raise Exception("Error message not found within 10 seconds.")

# Close the browser
driver.quit()