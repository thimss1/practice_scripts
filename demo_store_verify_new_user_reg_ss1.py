from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup Chrome WebDriver
driver = webdriver.Chrome()

# Go to the website
driver.get("http://demostore.supersqa.com")

# Click on My Account using correct XPath
my_account_xpath = "//nav[@id='site-navigation']//ul[@class='nav-menu']//a[@href='http://demostore.supersqa.com/my-account/']"
my_account_link = driver.find_element(By.XPATH, my_account_xpath)
my_account_link.click()

# Generate a unique email address
timestamp = str(time.time())
email = "rabbit" + timestamp + "@gmail.com"

# Register a new user using email and password
driver.find_element(By.ID, 'reg_email').send_keys(email)
driver.find_element(By.ID, 'reg_password').send_keys("Rabb01t!20Qa5")

# Click on "Register" button
register_button = driver.find_element(By.NAME, 'register')
register_button.click()

# Wait for the dashboard link to be visible
dashboard_link_xpath = "//a[contains(@class, 'woocommerce-MyAccount-navigation-link--dashboard') and contains(@class, 'is-active')]"
dashboard_link = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, dashboard_link_xpath)))

# Verify if the dashboard link is displayed
is_dashboard_link_displayed = dashboard_link.is_displayed()

# Print the result
if is_dashboard_link_displayed:
    print("Dashboard link is present.")
else:
    print("Dashboard link is not present.")


