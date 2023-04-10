import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Chrome Driver
serv_obj = ChromeService("webdrivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(5)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

action = ActionChains(driver)
# action.click_and_hold()
# action.context_click()
# action.double_click()
# action.drag_and_drop()
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".mouse-hover-content")))
# action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()

time.sleep(5)

