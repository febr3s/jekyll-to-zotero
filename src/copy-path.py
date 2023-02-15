from selenium import webdriver
import pyperclip

# Start a new instance of the Chrome driver
driver = webdriver.Chrome()

# Get the list of window handles
handles = driver.window_handles

# Switch to the desired window
for handle in handles:
    driver.switch_to.window(handle)
    # Check if the current window is the desired window
    if "Cuentos | MOREL" in driver.title:
        break

# Get the URL of the current tab
current_url = driver.current_url

# Copy the URL to the clipboard
pyperclip.copy(current_url)

# Store the URL in an array
url_list = [pyperclip.paste()]

print(url_list)

# Close the driver instance
driver.quit()