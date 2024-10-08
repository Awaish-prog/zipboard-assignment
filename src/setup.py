from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class SetUp:
    _driver = None
    _wait = None

    def __init__(self):
        self._driver = webdriver.Chrome()
        self._wait = WebDriverWait(self._driver, 30)

    def get_driver(self):
        return self._driver

    def get_wait(self):
        return self._wait

    def quit_driver(self):
        self._driver.quit()
