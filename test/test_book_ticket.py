import pytest

from page.book_ticket_page import BookTicket
from page.genericFunctions import GenericFunctions


@pytest.mark.usefixtures("setup", "before_test", "launch_application")
class TestDocumentCreation:

    @pytest.fixture(autouse=True)
    def class_objects(self):
        self.gf = GenericFunctions(self.driver)
        self.bt = BookTicket(self.driver)

    def test_BookTicket(self):
        self.bt.select_origin()
        self.bt.select_destination()
        self.bt.select_date()
        self.bt.click_search_button()
        self.bt.verify_correct_origin_destination_selected()




