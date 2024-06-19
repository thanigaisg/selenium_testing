from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utilities.Util import Util
from pageObjects.HomePage import HomePage
import pytest, copy

class Test_HomePage(Util):

    credents = []

    def test_login_credentials(self):
        homepage = HomePage(self.driver)
        credentials = homepage.getLoginCredentials()
        Test_HomePage.credents = copy.copy(credentials)
        print(credentials.__str__())
        assert "standard_user" in credentials, "standard_user is login credentials"

    def test_login_password(self):
        homepage = HomePage(self.driver)
        password = homepage.getLoginPassword()
        print(password.__str__())
        assert "secret_sauce" in password, "Password is verified"

    @pytest.mark.parametrize("credential", ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user', 'error_user', 'visual_user'])
    def test_successful_login(self, credential):
        homepage = HomePage(self.driver)
        password = homepage.getLoginPassword()
        homepage.getUserName().clear()
        homepage.getUserName().send_keys(credential)
        homepage.getPassword().clear()
        homepage.getPassword().send_keys(password[0])
        homepage.getLoginBtn().click()

        if credential != "locked_out_user":
            wait = WebDriverWait(self.driver, 20)
            wait.until(expected_conditions.presence_of_element_located(HomePage.product_container))

            assert homepage.getProductContainer() is not None

            assert homepage.getProductText() == "Products"

            assert homepage.showMenuItems() is not None

            homepage.processLogout()
        else:
            assert "Sorry, this user has been locked out" in homepage.getErrorMsg()




    
