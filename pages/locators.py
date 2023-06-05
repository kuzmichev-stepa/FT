from selenium.webdriver.common.by import By

class MainPageLocators():
    pass
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME_ON_PAGE = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_PRICE_ON_PAGE = (By.CSS_SELECTOR, "p.price_color")    
    BOOK_NAME_IN_MESSAGE = (By.CSS_SELECTOR, ".alert-safe:nth-child(1) strong")
    BOOK_PRICE_IN_MESSAGE = (By.CSS_SELECTOR, ".alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success:nth-child(1)")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a")

class BasketPageLocators():
    BASKET_TITLE = (By.CSS_SELECTOR, ".basket-title")
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p")