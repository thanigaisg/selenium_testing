import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.firefox.service import Service as FirefoxService

# Firefox Driver
serv_obj = FirefoxService("webdrivers\geckodriver_v0_32_0-win32\geckodriver.exe")
driver = webdriver.Firefox(service=serv_obj)
driver.implicitly_wait(2)

driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element(By.LINK_TEXT, "Click Here").click()

windows_opened = driver.window_handles

driver.switch_to.window(windows_opened[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close()

driver.switch_to.window(windows_opened[0])
assert driver.find_element(By.TAG_NAME, "h3").text == "Opening a new window"

time.sleep(2)

driver.close()