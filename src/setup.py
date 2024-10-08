import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from page_models.login_page import LoginPage
from page_models.dashboard_page import DashboardPage
from selenium.webdriver.support import expected_conditions as EC


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
        found_element: WebElement = self.get_wait().until(
            EC.any_of(
                EC.presence_of_element_located(LoginPage().get_email_locator()),
                EC.presence_of_element_located(DashboardPage().get_create_project())
            )
        )
        if found_element.get_attribute("type") == "button":
            return
        login_page = LoginPage()
        login_page.enter_email("awaishkhan79@gmail.com", self.get_wait())
        login_page.enter_password("ZipboardPassword@12", self.get_wait())
        login_page.click_login(self.get_wait())

    def quit_driver(self):
        self._driver.quit()
