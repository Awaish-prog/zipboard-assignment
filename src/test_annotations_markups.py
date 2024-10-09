from setup import SetUp
from user_actions import UserActions
from page_models.document_page import DocumentPage


class TestAnnotationsMarkUps:
    setup = SetUp()

    def test_annotations(self) -> None:
        user_actions: UserActions = UserActions()
        user_actions.login(self.setup)
        user_actions.navigate_to_document(self.setup, "Zipboard-assignment", "js_filename_9ZfQfYs5KbX5iD4Fv")
        document: DocumentPage = DocumentPage()
        assert document.add_note_to_document(self.setup.get_driver(), self.setup.get_wait(), "note"), "Failed to add Note to the PDF"
        document.delete_note(self.setup.get_driver(), self.setup.get_wait())

    def test_markups(self) -> None:
        user_actions: UserActions = UserActions()
        user_actions.login(self.setup)
        user_actions.navigate_to_document(self.setup, "Zipboard-assignment", "js_filename_9ZfQfYs5KbX5iD4Fv")
        document: DocumentPage = DocumentPage()
        assert document.add_line_to_document(self.setup.get_driver(), self.setup.get_wait()), "Failed to add line to the PDF"
        document.delete_line(self.setup.get_driver(), self.setup.get_wait())
