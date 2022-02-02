from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.HomePage import HomePage


class LoginPage(BasePage):
    """By_locators - or"""

    EMAIL = (By.XPATH, '//*[@id="user-name"]')
    PASSWORD = (By.XPATH, '//*[@id="password"]')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="login-button"]')
    # SIGH_UP = (By.LINK_TEXT, 'Sign up')

    '''constructor of the page class'''

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    '''Page Actions for LoginPage'''

    '''this is used to get a page title'''

    def get_login_page_title(self, title):
        return self.get_title(title)

    '''this is used to check a sign link'''

    def is_signup_link_exist(self):
        return self.is_visible(self.SIGH_UP)

    '''this is used to login the app'''

    def do_login(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        return HomePage(self.driver)
