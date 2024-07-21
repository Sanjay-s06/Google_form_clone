from selenium import webdriver
from selenium.webdriver.common.by import By

# Replace with the URL of your form
form_url = "http://localhost:8000/your-form.html"  # Assuming your form runs on a local server

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Open the form in the browser
driver.get(form_url)

# Find elements by their IDs (replace with actual element IDs from your form)
name_field = driver.find_element(By.ID, "name")
email_field = driver.find_element(By.ID, "email")
phone_field = driver.find_element(By.ID, "phone")
# ... add similar lines for other fields

# Enter sample data (replace with logic to generate test data)
name_field.send_keys("John Doe")
email_field.send_keys("test@example.com")
phone_field.send_keys("1234567890")
# ... fill other fields with test data

# Find the submit button (replace with actual selector if needed)
submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")

# Click the submit button
submit_button.click()

# Optional: Wait for a confirmation message or page change before closing
# time.sleep(5)  # Wait for 5 seconds (adjust as needed)

# Close the browser window
driver.quit()
