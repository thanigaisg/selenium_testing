"""
Locators
"""
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Chrome Driver
serv_obj = ChromeService("webdrivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.maximize_window()
driver.get("http://rahulshettyacademy.com/angularpractice/")

#ID, XPath, CSS-Selector, Classname, Name, linktext
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.ID, "inlineRadio1").click()

# Static Dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
# dropdown.select_by_value()

# XPath - //tagname[@attribute='value']
driver.find_element(By.XPATH, "//input[@value='Submit']").click()

# CSS-Selector - tagname[attribute='value'], #id, .class
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Selenium_Automation")

message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success!" in message

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Hello!")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()

time.sleep(5)