import time

from setup import SetUp
from user_actions import UserActions


class TestAnnotationsMarkUps:
    setup = SetUp()

    def test_annotations(self):
        UserActions().login(self.setup)

    def test_markups(self):
        UserActions().login(self.setup)

