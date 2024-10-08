from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:

    def __init__(self):
        self.create_project = (By.ID, '//button[span[text()="Create Project"]]')

    def get_create_project(self):
        return self.create_project
