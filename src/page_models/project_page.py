from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ProjectPage:

    def __init__(self, title: str):
        self.title: str = title
        self.review_button: tuple[str, str] = (By.XPATH, '//button[contains(text(),"Review")]')

    def get_title(self) -> str:
        return self.title

    def get_review_button(self) -> tuple[str, str]:
        return self.review_button

    def get_project_locator(self) -> tuple[str, str]:
        return By.XPATH, f'//h3[@title="{self.get_title()}"]'

    def open_project(self, wait: WebDriverWait) -> None:
        wait.until(EC.presence_of_element_located(self.get_project_locator())).click()

    def show_document_pop_up(self, wait: WebDriverWait, file_id: str) -> None:
        wait.until(EC.presence_of_element_located((By.ID, file_id))).click()

    def click_review(self, wait: WebDriverWait) -> None:
        wait.until(EC.presence_of_element_located(self.get_review_button())).click()
