import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Chrome Driver
serv_obj = ChromeService("webdrivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(2)

expected_products = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
actual_products = []
l
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)

results = driver.find_elements(By.XPATH, "//div[@class= 'products']/div")
count = len(results)
assert count > 0

for result in results:
    actual_products.append(result.find_element(By.CSS_SELECTOR, "h4").text)
    result.find_element(By.CSS_SELECTOR, "div button").click()

print("Expected Products : {}".format(expected_products))
print("Actual Products : {}".format(actual_products))

assert expected_products.sort() == actual_products.sort()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# Sum Validation
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")

sum_price = 0

for price in prices:
    sum_price += int(price.text)

tot_amount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert sum_price == tot_amount

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

discount = int(driver.find_element(By.CLASS_NAME, "discountPerc").text[:-1])

dis_amount = float(driver.find_element(By.CLASS_NAME, "discountAmt").text)

assert dis_amount == (tot_amount-(tot_amount/discount))
print("Discount Verified!")

time.sleep(5)