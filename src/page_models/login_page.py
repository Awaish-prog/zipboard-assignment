from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self):
        self.email_input = (By.ID, "login-username")
        self.password_input = (By.ID, "login-password")
        self.login_button = (By.XPATH, '//button[@id="login"]')

    def enter_email(self, email: str, wait: WebDriverWait):
        wait.until(EC.presence_of_element_located(self.email_input)).send_keys(email)

    def enter_password(self, password: str, wait: WebDriverWait):
        wait.until(EC.presence_of_element_located(self.password_input)).send_keys(password)

    def click_login(self, wait: WebDriverWait):
        wait.until(EC.element_to_be_clickable(self.login_button)).click()
