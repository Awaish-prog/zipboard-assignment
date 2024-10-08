import time

from setup import SetUp
from user_actions import UserActions


class TestAnnotationsMarkUps:
    setup = SetUp()

    def test_annotations(self):
        user_actions = UserActions()
        user_actions.login(self.setup)
        user_actions.navigate_to_document(self.setup, "Zipboard-assignment", "js_filename_TwpKGFqNGJydCEe52")


    def test_markups(self):
        user_actions = UserActions()
        user_actions.login(self.setup)

