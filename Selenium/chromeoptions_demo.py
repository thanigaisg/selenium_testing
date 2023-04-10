import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

# Chrome Driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

serv_obj = ChromeService("webdrivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj, options=chrome_options)
driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)