from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    username = (By.ID, "user-name")
    password = (By.CSS_SELECTOR, "#password")
    login_btn = (By.NAME, "login-button")
    login_credentials = (By.XPATH, "//div[@class='login_credentials']")
    login_password = (By.CSS_SELECTOR, "div[class='login_password']")
    product_container = (By.CLASS_NAME, "header_secondary_container")
    product_text = (By.XPATH, "//div/span")
    menu_btn = (By.ID, "react-burger-menu-btn")
    menu_items = (By.CSS_SELECTOR, ".bm-menu")
    logout_link = (By.ID, "logout_sidebar_link")
    err_msg = (By.XPATH,"//h3")

    def getUserName(self):
        return self.driver.find_element(*HomePage.username)
    
    def getPassword(self):
        return self.driver.find_element(*HomePage.password)
    
    def getLoginBtn(self):
        return self.driver.find_element(*HomePage.login_btn)
    
    def getLoginCredentials(self):
        user = self.driver.find_element(*HomePage.login_credentials)
        return user.text.split("\n")[1:]
    
    def getLoginPassword(self):
        password = self.driver.find_element(*HomePage.login_password)
        return password.text.split("\n")[1:]
    
    def getProductContainer(self):
        return self.driver.find_element(*HomePage.product_container)
    
    def getProductText(self):
        return self.getProductContainer().find_element(*HomePage.product_text).text
    
    def showMenuItems(self):

        self.driver.find_element(*HomePage.menu_btn).click()

        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(HomePage.menu_items))

        return self.driver.find_element(*HomePage.menu_items)

    def processLogout(self):
        self.driver.find_element(*HomePage.logout_link).click()

    def getErrorMsg(self):
        return self.driver.find_element(*HomePage.err_msg).text


