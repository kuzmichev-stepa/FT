from selenium.webdriver.common.by import By
from .base_page import BasePage

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME_ON_PAGE = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_PRICE_ON_PAGE = (By.CSS_SELECTOR, "p.price_color")    
    BOOK_NAME_IN_MESSAGE = (By.CSS_SELECTOR, ".alert-safe:nth-child(1) strong")
    BOOK_PRICE_IN_MESSAGE = (By.CSS_SELECTOR, ".alertinner p strong")
