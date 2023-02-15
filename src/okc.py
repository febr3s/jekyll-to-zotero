from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Start web driver
driver = webdriver.Firefox()

# Execute Action A
for i in range(20):
    driver.find_element_by_tag_name('body').send_keys(Keys.TAB)
driver.find_element_by_tag_name('body').send_keys("Querida, como podrás ver, dadas tus evidentes cualidades, voy a invitarte a acompañarme en alguno de los maravillosos momentos que a diario creo para mí.\n\nAtentamente,\n\nE.")
driver.find_element_by_tag_name('body').send_keys(Keys.TAB)

# Execute Action B
for i in range(33):
    driver.find_element_by_tag_name('body').send_keys(Keys.TAB)

# Repeat Action 2
while True:
    driver.find_element_by_tag_name('body').send_keys("Querida, como podrás ver, dadas tus evidentes cualidades, voy a invitarte a acompañarme en alguno de los maravillosos momentos que a diario creo para mí.\n\nAtentamente,\n\nE.")
    driver.find_element_by_tag_name('body').send_keys(Keys.TAB)
    if driver.execute_script("return document.activeElement.tagName") != 'INPUT':
        break