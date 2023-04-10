import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

# Chrome Driver
serv_obj = ChromeService("webdrivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute('value') == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break

radiobuttons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")

for radiobutton in radiobuttons:
    if radiobutton.get_attribute('value') == "radio2":
        radiobutton.click()
        assert radiobutton.is_selected()

radiobuttons[2].click()
assert radiobuttons[2].is_selected()

assert driver.find_element(By.ID, 'displayed-text').is_displayed()

driver.find_element(By.ID, 'hide-textbox').click()

assert not driver.find_element(By.ID, 'displayed-text').is_displayed()

time.sleep(5)