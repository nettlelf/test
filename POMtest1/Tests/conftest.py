import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from Config.config import TestData


@pytest.fixture(params=['chrome', 'firefox'], scope='class')
def init_driver(request):
    options = Options()
    options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    if request.param == 'chrome':
        web_driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
    if request.param == 'firefox':
        web_driver = webdriver.Firefox(executable_path=TestData.FIREFOX_EXECUTABLE_PATH, options=options)
    request.cls.driver = web_driver
    yield #здесь происходит тестирование
    web_driver.close()
