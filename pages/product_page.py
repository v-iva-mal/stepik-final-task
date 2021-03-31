from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def adding_to_basket_from_the_product_page(self):
        self.adding_to_basket_and_check_success_message()
        self.message_product_added_to_basket()
        self.message_basket_cost()

    def adding_to_basket_and_check_success_message(self):
        self.add_to_basket()
        self.solve_quiz_and_get_code()

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def message_product_added_to_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message_text_added_to_basket = self. browser.find_element(*ProductPageLocators.PRODUCT_ADDED_TO_BASKET).text
        assert product_name == message_text_added_to_basket, f"The name of the product in the message is different from the product that was added to basket"

    def message_basket_cost(self):
        product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_COST).text
        message_text_basket_cost = self.browser.find_element(*ProductPageLocators.BASKET_COST).text
        assert product_cost == message_text_basket_cost, f"The cost of the basket is not the same as the price of the product."

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message displays, but it should hide"