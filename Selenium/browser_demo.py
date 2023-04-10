"""
Demo Browser
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as MSEdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService

# Chrome Driver
serv_obj = ChromeService("webdrivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

# Firefox Driver
# serv_obj = FirefoxService("webdrivers\geckodriver_v0_32_0-win32\geckodriver.exe")
# driver = webdriver.Firefox(service=serv_obj)

# Microsoft Edge Driver
# serv_obj = MSEdgeService("webdrivers\edgedriver_win64\msedgedriver.exe")
# driver = webdriver.Edge(service=serv_obj)

driver.maximize_window()
driver.get("http://rahulshettyacademy.com")
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/consulting")
driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
driver.close()