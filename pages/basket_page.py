from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_TITLE),\
            "Basket isn't empty, but should be"
    
    def should_be_message_about_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY_BASKET),\
            "Message about basket is empty isn't presented, but should be"
