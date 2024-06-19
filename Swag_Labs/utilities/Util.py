import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures('setup')
class Util:

    def verifyPresenceElements(self, webelements):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(webelements))

    def selectOptionbytext(self, locator, text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)