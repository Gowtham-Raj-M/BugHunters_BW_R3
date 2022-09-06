import time
from datetime import timedelta, date

import allure

from base.basePage import BasePage
from constants import generic_constants as GC
from page.genericFunctions import GenericFunctions


class DocumentPage(BasePage):
    """
    This class of consists of reusable functions
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.gf = GenericFunctions(self.driver)

    @allure.step("launch zara website")
    def launch_zara_website(self):
        self.launch_url(GC.ZARA_URL)

    @allure.step("navigate to man section")
    def navigate_to_men_section(self):
        self.click(GC.ZARA_SEARCH_BAR)
        self.wait_for_element(GC.ZARA_DRESS_TEXT)
        self.click(GC.ZARA_DRESS_TEXT)
        self.wait_for_element(GC.ZARA_MAN)
        self.click(GC.ZARA_MAN)

    def capture_text_of_the_product(self):
        products = self.get_text(GC.ZARA_MAN_PRODUCTS)
        print(products)

    @allure.step("add to cart")
    def select_product_randomly_and_add_to_cart(self):
        self.wait_until_element_is_clickable(GC.SELECT_PRODUCT_ZARA_MEN)
        self.click(GC.SELECT_PRODUCT_ZARA_MEN)
        self.wait_for_element(GC.ZARA_ADD_TO_CART_BUTTON)
        self.click(GC.ZARA_ADD_TO_CART_BUTTON)
        validate = self.get_text(GC.VALIDATE_ERROR_MSG)
        assert validate == GC.ERROR_MSG
        self.click(GC.ZARA_CLOSE_BUTTON)
        self.wait_for_element(GC.SIZE_L)
        self.click(GC.SIZE_L)
        self.click(GC.ZARA_ADD_TO_CART_BUTTON)
        self.wait_for_element(GC.POPUP_CLOSE_BUTTON)
        self.click(GC.POPUP_CLOSE_BUTTON)

    def navigate_to_women_section(self):
        self.click(GC.ZARA_SEARCH_BAR)
        self.wait_for_element(GC.ZARA_DRESS_TEXT)
        self.click(GC.ZARA_DRESS_TEXT)
        self.wait_until_element_is_clickable(GC.FILTERS)
        self.click(GC.FILTERS)
        self.click(GC.PLUS_BUTTON)
        self.wait_for_element(GC.SELECT_SIZE_WOMEN)
        self.click(GC.SELECT_SIZE_WOMEN)
        self.wait_until_element_is_clickable(GC.FIRST_PRODUCT)
        self.click(GC.FIRST_PRODUCT)
        self.click(GC.FIRST_SIZE_FOR_WOMEN)


