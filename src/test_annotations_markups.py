import time

from setup import SetUp
from user_actions import UserActions
from page_models.document_page import DocumentPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestAnnotationsMarkUps:
    setup = SetUp()

    def test_annotations(self):
        user_actions = UserActions()
        user_actions.login(self.setup)
        user_actions.navigate_to_document(self.setup, "Zipboard-assignment", "js_filename_TwpKGFqNGJydCEe52")
        document = DocumentPage()
        document.add_note_to_document(self.setup.get_driver(), self.setup.get_wait(), "note")

    def test_markups(self):
        user_actions = UserActions()
        user_actions.login(self.setup)
