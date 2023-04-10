import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

# Chrome Driver
serv_obj = ChromeService("webdrivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(2)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
driver.get_screenshot_as_file("miscellaneous.png")

# Sort Web Tables
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

veggies_webelements = driver.find_elements(By.XPATH, "//tr/td[1]")
browser_sorted_veggies = [ele.text for ele in veggies_webelements]
org_browser_sorted_veggies = browser_sorted_veggies.copy()

browser_sorted_veggies.sort()

print("Sorted Veggies: {}".format(browser_sorted_veggies))

assert org_browser_sorted_veggies == browser_sorted_veggies

time.sleep(2)