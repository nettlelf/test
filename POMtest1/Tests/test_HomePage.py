from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from Pages.HomePage import HomePage


class Test_Home(BaseTest):

    def test_home_page_title(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.homePage.refresh_page(self)
