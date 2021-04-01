from .base_page import BasePage
from .locators import BasketPageLocatirs
from .locators import BasePageLocators
import pytest

class BasketPage(BasePage):
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocatirs.BASKET_ADD_PRODUCT), \
            "There are product(s) in the basket, but they should not be there"

        language = self.browser.find_element(*BasePageLocators.LANGUAGE).get_attribute("value")
        if language =="en-gb":
            busket_empty = self.browser.find_element(*BasketPageLocatirs.BASKET_EMPTY).text
            assert busket_empty == "Your basket is empty. Continue shopping", "The basket should be empty, but it contains product"
        else:
            raise pytest.UsageError("--The test assumes on website  British English the language")


