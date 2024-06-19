import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as MSEdgeService
from selenium.webdriver.common.by import By

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
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    request.cls.driver = driver

    yield

    driver.close()