"""
Locators
"""
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

# Chrome Driver
serv_obj = ChromeService("webdrivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/client")
driver.find_element(By.LINK_TEXT, "Forgot password?").click()

driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("hello@selenium.com")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("Password@123")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Password@123")
# driver.find_element(By.XPATH, "//button[@type='submit']").click()
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()

time.sleep(5)
