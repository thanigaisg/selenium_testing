import pytest
from  selenium import webdriver
from selenium.webdriver.edge.service import Service as MSEdgeService

driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="edge"
    )

@pytest.fixture()
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