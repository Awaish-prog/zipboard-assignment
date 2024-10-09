from selenium.webdriver.common.by import By


class ExplorerPage:

    def __init__(self):
        self.create_project: tuple[str, str] = (By.ID, '//button[span[text()="Create Project"]]')

    def get_create_project(self) -> tuple[str, str]:
        return self.create_project
