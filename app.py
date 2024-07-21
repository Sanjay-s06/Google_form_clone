from selenium import webdriver
from selenium.webdriver.common.by import By

# Replace with the URL of your form
form_url = "http://127.0.0.1:5500/form.html"  # Assuming your form runs on a local server

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Open the form in the browser
driver.get(form_url)

# Find elements by their IDs 
name_field = driver.find_element(By.ID, "name")
usn_field = driver.find_element(By.ID, "usn")
email_field = driver.find_element(By.ID, "email")
gender_field = driver.find_element(By.ID, "gender")
phone_field = driver.find_element(By.ID, "phone")
username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")

# ... add similar lines for other fields

# Enter sample data (replace with logic to generate test data)
name_field.send_keys("Anonymous")
usn_field.send_keys("4JN21IS200")
email_field.send_keys("user@gmail.com")
phone_field.send_keys("1234567890")
username_field.send_keys("Anonymous_06")
password_field.send_keys("Anonymous@06")

select_gender = Select(gender_field)

# ... fill other fields with test data

# Find the submit button (replace with actual selector if needed)
submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")

# Click the submit button
submit_button.click()

# Optional: Wait for a confirmation message or page change before closing
# time.sleep(5)  # Wait for 5 seconds (adjust as needed)

# Close the browser window
driver.quit()
