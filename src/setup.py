from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class SetUp:
    _driver = None
    _wait = None

    def __init__(self):
        self._driver = webdriver.Chrome()
        self._wait = WebDriverWait(self._driver, 30)

    def get_driver(self) -> webdriver.Chrome:
        return self._driver

    def get_wait(self) -> WebDriverWait:
        return self._wait

    def quit_driver(self) -> None:
        self._driver.quit()

    def switch_to_window(self, window_index: int) -> None:
        window_handle: str = self.get_driver().window_handles[window_index]
        self.get_driver().switch_to.window(window_handle)