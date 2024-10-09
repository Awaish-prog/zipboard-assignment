from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self):
        self.email_input: tuple[str, str] = (By.ID, "login-username")
        self.password_input: tuple[str, str] = (By.ID, "login-password")
        self.login_button: tuple[str, str] = (By.XPATH, '//button[@id="login"]')
        self.base_url: str = "https://app.zipboard.co"

    def enter_email(self, email: str, wait: WebDriverWait) -> None:
        wait.until(EC.presence_of_element_located(self.email_input)).send_keys(email)

    def enter_password(self, password: str, wait: WebDriverWait) -> None:
        wait.until(EC.presence_of_element_located(self.password_input)).send_keys(password)

    def click_login(self, wait: WebDriverWait) -> None:
        wait.until(EC.element_to_be_clickable(self.login_button)).click()
        wait.until(EC.url_contains(f'{self.get_base_url()}/explorer'))

    def get_email_locator(self) -> tuple[str, str]:
        return self.email_input

    def get_base_url(self) -> str:
        return self.base_url
