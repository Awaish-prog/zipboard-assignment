import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from page_models.login_page import LoginPage


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

    def login(self):
        self.get_driver().get("https://app.zipboard.co")
        login_page = LoginPage()
        login_page.enter_email("awaishkhan79@gmail.com", self.get_wait())
        login_page.enter_password("ZipboardPassword@12", self.get_wait())
        login_page.click_login(self.get_wait())
        time.sleep(20)

    def quit_driver(self):
        self._driver.quit()
