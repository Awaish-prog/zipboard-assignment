import time

from selenium.webdriver.remote.webelement import WebElement
from page_models.login_page import LoginPage
from page_models.explorer_page import ExplorerPage
from page_models.project_page import ProjectPage
from selenium.webdriver.support import expected_conditions as EC
from setup import SetUp


class UserActions:

    def login(self, setup: SetUp):
        setup.get_driver().get("https://app.zipboard.co")
        found_element: WebElement = setup.get_wait().until(
            EC.any_of(
                EC.presence_of_element_located(LoginPage().get_email_locator()),
                EC.presence_of_element_located(ExplorerPage().get_create_project())
            )
        )
        if found_element.get_attribute("type") == "button":
            return
        login_page = LoginPage()
        login_page.enter_email("awaishkhan79@gmail.com", setup.get_wait())
        login_page.enter_password("ZipboardPassword@12", setup.get_wait())
        login_page.click_login(setup.get_wait())

    def navigate_to_document(self, setup: SetUp, project_title, file_id):
        projectPage: ProjectPage = ProjectPage(project_title)
        projectPage.open_project(setup.get_wait())
        projectPage.show_document_pop_up(setup.get_wait(), file_id)
        projectPage.click_review(setup.get_wait())

