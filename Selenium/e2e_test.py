import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Chrome Driver
serv_obj = ChromeService("webdrivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

# //a[contains(@href, 'shop')]   a[href*='shop']
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()

products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for product in products:
    if "blackberry" in product.find_element(By.CSS_SELECTOR, "div h4 a").text.lower():
        product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

driver.find_element(By.ID, "country").send_keys("ind")

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".suggestions")))

countries = driver.find_elements(By.CSS_SELECTOR, ".suggestions")
for country in countries:
    country_name = country.find_element(By.XPATH, "ul/li/a")
    if "india" in country_name.text.lower():
        country_name.click()
        break

driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()

driver.find_element(By.CSS_SELECTOR, "input[class~=btn-success]").click()

assert "Success! Thank you!" in driver.find_element(By.CSS_SELECTOR, "div[class*='alert-success']").text

time.sleep(2)