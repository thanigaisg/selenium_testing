import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

# Chrome Driver
serv_obj = ChromeService("webdrivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.CSS_SELECTOR, "#name").send_keys("Selenium Learner!")
driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()

alert = driver.switch_to.alert
print(alert.text)

assert "Selenium Learner!" in alert.text

alert.accept()

driver.find_element(By.CSS_SELECTOR, "#confirmbtn").click()

alert1 = driver.switch_to.alert
print(alert1.text)

alert.dismiss()

time.sleep(5)