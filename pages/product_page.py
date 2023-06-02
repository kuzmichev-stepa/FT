from .base_page import BasePage
from .locators import ProductPageLocators

###todo вынести определение имени и цены в отдельный метод до добавления в корзину

class ProductPage(BasePage):    
    def add_product_to_basket(self):
        btn_add_to_basket = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        btn_add_to_basket.click()
    
    def should_be_messages_on_page(self):
        self.should_be_message_with_product_name()
        self.should_be_message_with_product_price()
    
    def should_be_message_with_product_name(self):
        book_name_on_page = (self.browser.find_element(*ProductPageLocators.BOOK_NAME_ON_PAGE)).text
        book_name_in_message = (self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_MESSAGE)).text
        assert book_name_on_page == book_name_in_message, \
            f"Price in confirm message - '{book_name_in_message}', instead '{book_name_on_page}'"
    
    def should_be_message_with_product_price(self):
        book_price_on_page = (self.browser.find_element(*ProductPageLocators.BOOK_PRICE_ON_PAGE)).text
        book_price_in_message = (self.browser.find_element(*ProductPageLocators.BOOK_PRICE_IN_MESSAGE)).text
        assert book_price_on_page == book_price_in_message, \
            f"Price in confirm message - '{book_price_in_message}', instead '{book_price_on_page}'"
