from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import pytest
import time

#@pytest.mark.parametrize('num', [*range(1,7), pytest.param(7, marks=pytest.mark.xfail(reason="Некорректен по условию задания")), *range(8,10)])
#def test_guest_can_add_product_to_basket(browser,num):
#    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}"
#    page = ProductPage(browser, link)
#    page.open()
#    page.add_product_to_basket()
#    page.solve_quiz_and_get_code()
#    page.should_be_messages_on_page()
#
#@pytest.mark.xfail(reason = "Некорректен по условию задания")    
#def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#    page = ProductPage(browser, link)
#    page.open()
#    page.add_product_to_basket()
#    page.should_not_be_success_message()
#    
#def test_guest_cant_see_success_message(browser):
#    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#    page = ProductPage(browser, link)
#    page.open()
#    page.should_not_be_success_message()
#
#@pytest.mark.xfail(reason = "Некорректен по условию задания")    
#def test_message_disappeared_after_adding_product_to_basket(browser):
#    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#    page = ProductPage(browser, link)
#    page.open()
#    page.add_product_to_basket()
#    page.should_be_disappeared_success_message()
#    
#def test_guest_should_see_login_link_on_product_page(browser):
#    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#    page = ProductPage(browser, link)
#    page.open()
#    page.should_be_login_link()
#
#def test_guest_can_go_to_login_page_from_product_page(browser):
#    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#    page = ProductPage(browser, link)
#    page.open()
#    page.go_to_login_page()
#    login_page = LoginPage(browser, browser.current_url)
#    login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_is_empty()
    basket_page.should_be_message_about_basket_is_empty()

if __name__ == "__main__":
    pytest.main()