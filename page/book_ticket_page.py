import time
from datetime import timedelta, date

import allure

from base.basePage import BasePage

from constants import book_ticket_constants as BT
from page.genericFunctions import GenericFunctions


class BookTicket(BasePage):
    """
    This class of consists of reusable functions which can be used in Document creation and submission flow
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.gf = GenericFunctions(self.driver)

    def select_origin(self):

        self.send_keys(BT.ORIGIN, BT.ORIGIN_VALUE)
        self.click(BT.ORIGIN_LIST)

    def select_destination(self):
        self.send_keys(BT.DESTINATION, BT.DESTINATION_VALUE)
        self.click(BT.DESTINATION_LIST)

    def select_date(self):
        self.click(BT.DEPARTUREDATE)
        self.click(BT.DATEPICKERNEXT)
        self.click(BT.DATE)
        time.sleep(2)

    def click_search_button(self):
        self.click(BT.SEARCHBUTTON)

    def verify_correct_origin_destination_selected(self):
        value = self.get_text_from_webelement(BT.LOCATION)
        self.get
        print(value)

    #  return value

    def select_element_from_list(self, locator, value):

        html_list = self.driver.find_elements_by_xpath(locator)

        print("html_list:", html_list)
        items = html_list.find_elements_by_xpath(locator)
        for item in items:
            text = item.text
            if value == text:
                print(text)
