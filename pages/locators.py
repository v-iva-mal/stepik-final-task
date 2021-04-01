from selenium.webdriver.common.by import By

class BasePageLocators():
    LANGUAGE = (By.CSS_SELECTOR, ".form-control>[selected='selected']")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocatirs():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group [class='btn btn-default']")
    BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner>p")
    BASKET_ADD_PRODUCT = (By.CSS_SELECTOR, "#basket_formset")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_COST = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_ADDED_TO_BASKET = (By.CSS_SELECTOR, ".alert-success:nth-child(1) strong")
    BASKET_COST = (By.CSS_SELECTOR, ".alert-info strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success:nth-child(1) .alertinner")