import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as MSEdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="edge"
    )

@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser = request.config.getoption("browser_name")

    if browser == "edge":
        serv_obj = MSEdgeService("..\\webdrivers\\edgedriver_win64\\msedgedriver.exe")
        driver = webdriver.Edge(service=serv_obj)

    driver.implicitly_wait(2)
    driver.get("https://paymentcardtools.com/")
    driver.maximize_window()

    request.cls.driver = driver

    yield

    driver.close()

@pytest.fixture(scope="class")
def tag_decoder(request):
    emv_tag_decoder = request.cls.driver.find_element(By.CSS_SELECTOR, "button[data-bs-target='#emv-tag-decoders-collapse']")
        
    if emv_tag_decoder.get_attribute('aria-expanded') == 'false':
        emv_tag_decoder.click()

@pytest.fixture(scope="class")
def tvr_decoder(request):

    emv_tags = request.cls.driver.find_elements(By.XPATH, "//div[@class='pb-1 collapse show']/ul/li")

    for ele in emv_tags:
        if ele.text == "TVR (Tag 95)":
            ele.click()
    wait = WebDriverWait(request.cls.driver, 10)
    wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@id='input-tvr']")))


    