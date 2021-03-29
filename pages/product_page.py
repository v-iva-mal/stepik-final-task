from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def adding_to_basket_from_the_product_page(self):
        self.add_to_basket()
        self.solve_quiz_and_get_code()
        self.message_product_added_to_basket()
        self.message_basket_cost()

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def message_product_added_to_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message_text_added_to_basket = self. browser.find_element(*ProductPageLocators.PRODUCT_ADDED_TO_BASKET).text
        assert self.is_element_present(*ProductPageLocators.PRODUCT_ADDED_TO_BASKET), "No message that the item has been added to basket"
        assert product_name in message_text_added_to_basket, f"The name of the product in the message is different from the product that was added to basket"

    def message_basket_cost(self):
        product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_COST).text
        message_text_basket_cost = self.browser.find_element(*ProductPageLocators.BASKET_COST).text
        assert self.is_element_present(*ProductPageLocators.BASKET_COST), "There is no message with the cost of the basket"
        assert product_cost in message_text_basket_cost, f"The cost of the basket is not the same as the price of the product."


