from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage
from Tests.test_base import BaseTest
from selenium.webdriver.support.ui import Select


 class HomePage(BaseTest):

    BUTTON1 = (By.XPATH, '//*[@id="27"]/div/div[1]/div/div[2]/div[5]/div/div/span')

    def __init__(self, driver):
        super().__init__(driver)

    def refresh_page(self):
        element = self.select.(self.BUTTON1)
        element.select_by_index(5)


