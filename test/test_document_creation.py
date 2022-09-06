import pytest

from constants import generic_constants as GC

from page.document_page import DocumentPage
from page.genericFunctions import GenericFunctions


@pytest.mark.usefixtures("setup", "before_test", "launch_application")
class TestDocumentCreation:

    @pytest.fixture(autouse=True)
    def class_objects(self):
        self.gf = GenericFunctions(self.driver)
        self.dp = DocumentPage(self.driver)

    def test_launch_zara_website_navigate_to_man_section(self):
        """
        Navigates to MAN section
        :return:
        """
        self.dp.navigate_to_men_section()
        self.dp.select_product_randomly_and_add_to_cart()
        self.dp.navigate_to_women_section()






